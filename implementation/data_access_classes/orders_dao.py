from mysql.connector import MySQLConnection

class OrdersDAO():
    def __init__(self):
        #Make sure to load user and password from a file that is not uploaded to github!
        self.connection = MySQLConnection(user='root', password='Revature-RootSQL-92',
                              host='127.0.0.1', 
                              database='myfirstdb')
        
