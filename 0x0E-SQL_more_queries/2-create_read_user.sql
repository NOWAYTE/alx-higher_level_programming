-- a script that grants user_0d_2 SELECT privilege on databse hbtn_0_2
CREATE DATABASE IF NOT EXISTS hbtn_0_2;
CREATE TABLE IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_pwd';
GRANT SELECT ON hbtn_0_2.* TO user_0d_1;
FLUSH PRIVILEGES;