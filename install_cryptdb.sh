#! /bin/bash

if [[ "$OSTYPE" != "linux-gnu" ]]; then
	'/Applications/Docker/Docker Quickstart Terminal.app/Contents/Resources/Scripts/start.sh' | docker build -t cryptdb_server:v1 cryptdb_server/


# Build CryptDB Database Server
docker build -t cryptdb_server:v1 cryptdb_server/

# Build CryptDB Demo Application
docker build -t cryptdb_app:v1 cryptdb_app/

# Run database server
docker run -it --name cryptdb_server -p 3306:3306 -p 3307:3307 -e MYSQL_ROOT_PASSWORD="letmein" cryptdb:v1

sleep 5

# Run demo application
docker run -it --name cryptdb_app --link cryptdb_server cryptdb_app:v1

fi
