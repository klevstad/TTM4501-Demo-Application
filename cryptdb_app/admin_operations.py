import database, print_factory, mysql_procedures

def show_tables():
	result, headers = database.query_handler(mysql_procedures.SHOW_TABLES)
	print_factory.print_result(result, headers)
	raw_input("\n\n\n... Press any key to return to main menu.\n")


def show_contents_of_table():
	result, headers = database.query_handler(mysql_procedures.SHOW_TABLES)
	print_factory.print_result(result, headers)
	tablename = raw_input("\nPlease enter a valid tablename from the table above: ")

	while not valid_table_name(result, tablename) and len(tablename) != 0:
		tablename = raw_input("\nResearch shows that your suggested tablename is not real. Please provide from list above or <Enter> to exit: ")
	
	if len(tablename) != 0:

		query = "SELECT * FROM {0};".format(tablename)
		result, headers = database.query_handler(query)
		print_factory.print_result(result, headers)
	raw_input("\n\n\n... Press any key to return to main menu.\n")


def valid_table_name(result, tablename):
	for table in result:
		if tablename == table[0]:
			return True
	return False
