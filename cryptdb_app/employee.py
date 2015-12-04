class Employee:

	def __init__(self, empl_num, name, ssn, age, salary, division):
		self.empl_num = empl_num
		self.name = name.title()
		self.age = age
		self.ssn = ssn
		self.salary = salary
		self.division = division.title()



	def set_name(self, name):
		self.name = name.title()


	def set_age(self, age):
		self.age = age

	def set_ssn(self, ssn):
		self.ssn = ssn

	def set_salary(self, salary):
		self.salary = salary

	def set_division(self, division):
		self.division = division
