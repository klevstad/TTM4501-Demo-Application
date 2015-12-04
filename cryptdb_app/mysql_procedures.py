# Validated queries


CREATE_EMPLOYEE = "INSERT INTO employees VALUES ('', {0}, '{1}', {2}, {3}, {4}, '{5}');"

CREATE_EMPLOYEE_TABLE = "CREATE TABLE IF NOT EXISTS employees (ID INT NOT NULL AUTO_INCREMENT, Empl_Num INTEGER NOT NULL, Name VARCHAR(255), SocialSecNum VARCHAR(255), Age INTEGER, Salary INTEGER, Division VARCHAR(255), PRIMARY KEY (ID));"

GET_HIGHEST_EMPL_NUM = "SELECT MAX(Empl_Num) FROM employees;"

SELECT_ALL = "SELECT * FROM employees;"

SHOW_TABLES = "SHOW TABLES;"

UPDATE_EMPLOYEE = 'UPDATE employees SET {0}={1} WHERE id={2};'

# Not yet validated queries

DELETE_EMPLOYEE = 'DELETE FROM employee_table WHERE id = {0}'


# Helper methods
def insert_employee(employee):
	return CREATE_EMPLOYEE.format(employee.empl_num, employee.name, employee.ssn, employee.age, employee.salary, employee.division)


def update_employee(e_id, column, value):
	return UPDATE_EMPLOYEE.format(column, value, e_id)


def delete_employee(e_id):
	return DELETE_EMPLOYEE(e_id)
