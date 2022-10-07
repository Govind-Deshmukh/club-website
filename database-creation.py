import sqlite3

conn = conn = sqlite3.connect('database.db')

# CREATE TABLE `club_users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT , `name` VARCHAR NOT NULL , `email` VARCHAR NOT NULL , `mobile` VARCHAR NOT NULL , `domain` VARCHAR NOT NULL , `year` VARCHAR NOT NULL , `password` VARCHAR NOT NULL ) ; 