FROM python:2.7

MAINTAINER Eirik Klevstad

# Update and install mysql API for python
RUN apt-get update
RUN apt-get install -y python-mysqldb
RUN pip install MySQL-python
RUN mkdir -p /demo/code

# Add code
ADD admin_operations.py /demo/code/admin_operations.py
ADD database.py 		/demo/code/database.py
ADD employee.py 		/demo/code/employee.py
ADD mysql_procedures.py /demo/code/mysql_procedures.py
ADD print_factory.py 	/demo/code/print_factory.py
ADD program.py 			/demo/code/program.py
ADD user.py 			/demo/code/user.py
ADD user_operations.py 	/demo/code/user_operations.py
ADD validator.py 		/demo/code/validator.py

# Add configuration file
ADD config.ini			/demo/code/config.ini

# Expose ports to outside applications.
EXPOSE 3306 3307

# Run the demo application
WORKDIR /demo/code
CMD [ "python", "./program.py" ]