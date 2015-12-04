def print_column_row(headers):
	column_string = "\n\n# |\t"
	for column_name in headers:
		column_string += column_name.upper() + "\t"

	print column_string + "\n"


def print_row(row_number, row):
	row_string = "{0} |\t".format(row_number)

	for item in row:
			row_string += str(item) + "\t"
	
	print row_string

def print_sqlop_error(e):
	print "\n[!!!] Error executing the query. Caught OperationalError:\n"
	print e
	print "\n[!!!] End\n"

def print_result(results, headers):

	if headers:
		print_column_row(headers)
	for row_number in range(0, len(results)):
		print_row(row_number + 1, results[row_number])

