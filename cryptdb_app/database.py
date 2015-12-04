#!/usr/bin/python
from contextlib import closing
import MySQLdb, sys, print_factory, ConfigParser, os, mysql_procedures

CONFIGURATION = "CryptDB"
DB_CONNECTION = None


def ConfigSectionMap(section):
	Config = ConfigParser.ConfigParser()
	Config.read(os.getcwd() + "/config.ini")
	dict1 = {}
	options = Config.options(section)
	for option in options:
		try:
			dict1[option] = Config.get(section, option)
			if dict1[option] == -1:
				DebugPrint("skip: %s" % option)
		except:
			print("exception on %s!" % option)
			dict1[option] = None
	return dict1


def load_config():
	global HOST, USER, PASSWORD, PORT, DATABASE

	config = ConfigSectionMap(CONFIGURATION)

	HOST = config['host']
	USER = config['username']
	PASSWORD = config['password']
	PORT = int(config['port'])
	DATABASE = config['database']

	print "=" * 80
	print "[***] Host address:\t{0}".format(HOST)
	print "[***] Port number:\t{0}".format(PORT)
	print "[***] Username:\t\t{0}".format(USER)
	print "[***] Password:\t\t{0}".format(PASSWORD)
	print "[***] Database:\t\t{0}".format(DATABASE)
	print "=" * 80

def create_db_if_not_exists():
	query_handler('CREATE DATABASE IF NOT EXISTS {0}'.format(DATABASE))
	query_handler('USE {0}'.format(DATABASE))
	query_handler(mysql_procedures.CREATE_EMPLOYEE_TABLE)
	
def setup_connection():
	'''
	Connect to a MYSQL-database with host address, port number and name of database if any.
	'''
	global DB_CONNECTION
	
	print "\n[***] Connecting to '{0}' through CryptDB Proxy on {1}:{2}".format(DATABASE, HOST, PORT)
	
	try:
		DB_CONNECTION = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, port=PORT)
		print "[***] Connection established :)"
		if DATABASE:
			query_handler("use {0}".format(DATABASE))
			print "\n[===] Current database is: '{0}'. Ready for queries".format(DATABASE)

	except Exception, e:
		print "\n[***] Connection failed :(\n"
		print "[***] Error message: {0}".format(str(e))
		exit(-1)


def query_handler(query):

	'''
	Delegate execution of query and handle exceptions. Contains a ninja hack to handle CryptDBs adjustable encryption layers which isses an UPDATE
	of the encryption level instead of the actual query. Need of retransmission of query and handle exception.
	'''

	with closing(DB_CONNECTION.cursor()) as cur:

		try:
			return execute_query(query, cur)

		except MySQLdb.OperationalError as err:
			# Insane ninja hack because of the layer adjusting in CryptDB.
			if 'proxy did rollback' in str(err):
				try:
					return execute_query(query, cur)
					
				except MySQLdb.OperationalError as err:
					# An even more insane hack for when joins are performed
					if 'proxy did rollback' in str(err):
						return execute_query(query, cur)

			return err, -1


def execute_query(query, cur):
	cur.execute(query)
	commit(query)

	results = cur.fetchall()
	headers = extract_column_headers(cur)

	return results, headers

def commit(query):
	'''
	Issues a commit if the query was INSERT, UPDATE or DELETE as cryptdb has autocommit=0 and needs manually commit.
	'''
	q = query.lower()
	if 'update' in q or 'insert' in q or 'delete' in q or 'create' in q:
		DB_CONNECTION.commit()
		print "\nSuccessfully committed.\n"


def switch_connection():
	global PORT
	close_connection(True)

	if PORT == 3306:
		PORT = 3307
	elif PORT == 3307:
		PORT = 3306
	else:
		pass

	setup_connection()



def close_connection(switch):
	DB_CONNECTION.close()
	if switch:
		print "\n[***] Switching connection"
	else:
		print "\n[***] Exit signal received. Closing connection"
		print "[***] Connection closed on {0}:{1}".format(HOST, PORT)


def extract_column_headers(cursor):
	'''
	Get column names from a query response
	'''
	if cursor.description:
		num_fields = len(cursor.description)
		#print cursor.description
		if num_fields > 0:
			return [i[0] for i in cursor.description]
