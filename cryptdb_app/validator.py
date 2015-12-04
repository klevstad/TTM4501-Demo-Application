def age_is_valid(age):
	if is_integer(age) and int(age) >= 15 and int(age) < 100:
		return True
	return False

def ssn_is_valid(ssn):
	return len(ssn) == 11

def salary_is_valid(salary):
	if is_integer(salary) and salary > 0:
		return True
	return False



# Helper methods
def is_integer(num):
	try:
		int(num)
		return True
	except ValueError:
		return False
