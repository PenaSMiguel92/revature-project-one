from mysql.connector import MySQLConnection

class AccountDAO():
    def __init__(self):
        self.connection = MySQLConnection(user='root', password='Revature-RootSQL-92',
                              host='127.0.0.1', 
                              database='myfirstdb')