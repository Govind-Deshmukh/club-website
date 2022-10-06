import mysql.connector


try:
    mydb = mysql.connector.connect(
    host = "remotemysql.com", # your host address (yourservice.com)
    user = "pvDhFaBOFP", # your yasername for sql database
    password = "AOATIK73jC", # your password 
    database = "pvDhFaBOFP" # your database name
    )
except Exception as e:
    print(e)

# cursor = mydb.cursor()


# cursor.execute(
#     '''CREATE TABLE user
#          (ID INT PRIMARY KEY     NOT NULL AUTO_INCREMENT,
#          name TEXT NOT NULL,
#          email TEXT NOT NULL,
#          domain TEXT NOT NULL,
#          educationalyear TEXT NOT NULL,
#         password TEXT NOT NULL
#         );'''
# )