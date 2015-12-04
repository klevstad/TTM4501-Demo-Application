import database, user_operations, admin_operations, print_factory

commands = [["Display employees' information", "Add employee", "Update employee", "Perform analyses", "Type your own queries", "Switch to Administrator", "Quit application"],
["View tables", "View contents of table", "Type your own queries", "Switch to CryptDB user", "Exit application"]]

USER_ROLE = 0 # 0 = User, 1 = Admin
ROLE_NAMES = ["CryptDB User", "Database Administrator"]



def main():
	database.load_config()
	database.setup_connection()
	database.create_db_if_not_exists()

	print_welcome()
	print_menu()
	command = take_command()
	while True:
		if USER_ROLE == 0:
			perform_user_command(command)
		else:
			perform_admin_command(command)
		print_menu()
		command = take_command()

def print_welcome():
	print "\n\n"
	print "=" * 80
	print "\n\n"
	print "\t\t\tWelcome to CryptDB Test 1.0\n\n"
	print "=" * 80

def print_menu():
	print "Currently logged in as a... {0}".format(ROLE_NAMES[USER_ROLE].upper())
	print "=" * 80
	print "\n\tMAIN MENU:\n"
	num = 0
	for command in commands[USER_ROLE]:
		print "\t\t{0}:\t{1}".format(num + 1, commands[USER_ROLE][num])
		num += 1

	print "\n\n\n"

def take_command():
	command = raw_input("Please enter your command number: ")

	while invalid_command(command):
		command = raw_input("Command invalid. Please enter your command number: ")

	return int(command)

def invalid_command(command):
	try:
		int(command)
		if int(command) > 0 and int(command) < len(commands[USER_ROLE]) + 1:
			return False
		return True
	except ValueError:
		return True

def perform_user_command(command):

	switcher = {
	1 : user_operations.display_employees,
	2 : user_operations.add_employee,
	3 : user_operations.update_employee,
	4 : user_operations.perform_analyses,
	5 : test_queries,
	6 : switch_role,
	7 : quit_application,
	}

	return switcher[command]()

def perform_admin_command(command):
	switcher = {
	1 : admin_operations.show_tables,
	2 : admin_operations.show_contents_of_table,
	3 : test_queries,
	4 : switch_role,
	5 : quit_application,
	}

	return switcher[command]()

# Program specific operations

def test_queries():
	q = raw_input("Enter query or hit <Enter> to return to main menu: ")
	while True:
		if len(q) == 0:
			return
		result, headers = database.query_handler(q)
		while headers == -1:
			print "\n[!!!] MySQLdb.OperationalError\n"
			print str(result)
			print "\n[!!!]"
			q = raw_input("It seems that your query was invalid. Check your syntax and try again, or hit <Enter> to escape.\n")
			if len(q) == 0:
				return
			result, headers = database.query_handler(q)
		
		print_factory.print_result(result, headers)
		q = raw_input("\n\n\n... Enter a new query or hit <Enter> to return to main menu: ")
		

def switch_role():
	global USER_ROLE
	database.switch_connection()

	if USER_ROLE == 0:
		USER_ROLE = 1
	else:
		USER_ROLE = 0

	print_welcome()

def quit_application():
	database.close_connection(False)
	print "\nThank you. Come again."
	exit(1)


main()