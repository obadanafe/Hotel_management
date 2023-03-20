FROM mysql:latest

# Set root password
ENV MYSQL_ROOT_PASSWORD=password

# Copy custom configuration file
#COPY my.cnf /etc/mysql/conf.d/my.cnf

# Copy initial SQL scripts to create database and user
COPY init_db.sql /docker-entrypoint-initdb.d/init_db.sql

# Expose MySQL port
EXPOSE 3306

