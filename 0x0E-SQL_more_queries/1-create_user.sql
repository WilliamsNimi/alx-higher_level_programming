-- create a user and grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
UPDATE mysql.user SET Password=PASSWORD('user_0d_1_pwd') WHERE USER='user_0d_1';