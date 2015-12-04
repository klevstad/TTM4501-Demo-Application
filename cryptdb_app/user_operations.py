import database, validator, print_factory, employee, mysql_procedures

def display_employees():
	results, headers = database.query_handler(mysql_procedures.SELECT_ALL)

	if results and headers:
		print_factory.print_result(results, headers)
	if not len(results) and headers:
		print "\n<Empty>\n"

	raw_input("\n\n\n... Press any key to return to main menu.\n")
	return

def add_employee():

	name = raw_input("Enter name of employee: ")
	while len(name) == 0:
		name = raw_input("No name. Enter name of employee: ")

	ssn = raw_input("Enter Social Security Number (SSN) of employee: ")
	while not validator.ssn_is_valid(ssn):
		ssn = raw_input("Invalid SSN. Enter Social Security Number (SSN) of employee: ")

	age = raw_input("Enter age of employee: ")
	while not validator.age_is_valid(age):
		age = raw_input("Invalid age. Enter age of employee: ")

	salary = raw_input("Enter salary of employee: ")
	while not validator.salary_is_valid(salary):
		salary = raw_input("Invalid salary. Enter salary of employee: ")

	division = raw_input("Enter division of employee: ")
	while len(division) == 0:
		division = raw_input("No division. Enter division of employee: ")

	result, headers = database.query_handler(mysql_procedures.GET_HIGHEST_EMPL_NUM)

	if result[0][0] == 'NULL':
		empl_num = 1 
	else:
		empl_num = int(result[0][0]) + 1

	new_employee = employee.Employee(empl_num, name, ssn, age, salary, division)

	insert_query = mysql_procedures.insert_employee(new_employee)
	database.query_handler(insert_query)

	print "\n{0} was added to table with employee number {1}.".format(name.title(), empl_num)

def update_employee():
	results, headers = database.query_handler(mysql_procedures.SELECT_ALL)

	if results and headers:
		print_factory.print_result(results, headers)
	if not len(results) and headers:
		print "There is no records in this table."
		return
	
	e_id = raw_input("Enter id of Employee: ")
	column = raw_input("Enter property to update: ")
	value = raw_input("Enter new value of {0}: ".format(column))

	update_query = mysql_procedures.update_employee(e_id, column, value)
	database.query_handler(update_query)

	print "Updated!"


def perform_analyses():
	print "NOT IMPLEMENTED"

