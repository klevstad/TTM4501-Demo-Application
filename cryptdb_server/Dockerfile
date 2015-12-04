FROM debian:wheezy

MAINTAINER Eirik Klevstad # Bai Xiaoyong "lostitle@gmail.com"

# make sure the package repository is up to date
RUN apt-get update

# Install stuff
RUN apt-get install -y ca-certificates supervisor sudo ruby git

RUN mkdir -p /var/log/supervisor

RUN echo 'root:root' |chpasswd

# Set Password of MySQL root
ENV MYSQL_PASSWORD letmein

# Install MySQL Server in a Non-Interactive mode. Default root password will be $MYSQL_PASSWORD
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PASSWORD" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PASSWORD" | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server

RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
RUN /usr/sbin/mysqld & sleep 10s && echo "GRANT ALL ON *.* TO root@'%' IDENTIFIED BY 'letmein' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql -uroot -pletmein

# Add VOLUMEs to allow backup of config and databases
#VOLUME  ["/var/test", "/var/lib/mysql"]

RUN git clone https://github.com/klevstad/cryptdb.git /opt/cryptdb
WORKDIR /opt/cryptdb

RUN ruby scripts/install.rb .

# Adding Script
ADD cryptdb.sh /opt/cryptdb.sh
RUN chmod 755 /opt/cryptdb.sh; ln -s /opt/cryptdb.sh /usr/bin/cryptdb.sh

RUN echo "\
[supervisord]\n\
nodaemon=true\n\
\n\
[program:mysql]\n\
command=service mysql start\n\
\n\
" > /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]

CMD ["/opt/cryptdb.sh", "start"]

EXPOSE 22 3306 3307
