from abc import ABC
import csv
import logging
import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from custom_exceptions.connection_failed import ConnectionFailed

class DataAccessObjectInterface(object):

    current_connection: MySQLConnection = None
    current_cursor: MySQLCursor = None

    def __init__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataAccessObjectInterface, cls).__new__(cls)
        return cls.instance

    @classmethod
    def get_cursor(class_pointer) -> MySQLCursor:
        """
            This method should be called from child class as super().get_cursor() which will in turn 
            call get_connection, and ensure that only one connection object and one cursor object are created.
        """
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        class_pointer.get_connection()
        if class_pointer.current_connection == None:
            raise ConnectionFailed("Please make sure the .csv file exists or the values are correct.")

        if class_pointer.current_cursor == None:
            try:
                class_pointer.current_cursor = class_pointer.current_connection.cursor()
            except (mysql.connector.ProgrammingError, ValueError) as mysql_error:
                
                return
        logging.info("Connected to database successfully.")
        return class_pointer.current_cursor
    
    @classmethod
    def get_connection(class_pointer) -> MySQLConnection:
        """
            Make sure to have a .csv file with user, password, host, and database columns in a directory called config/
            No quotes or spaces between.
        """
        logging.info('Attempting to connect...')
        try:
            filename = 'config/mysql_connection_vars.csv'
            with open(filename, 'r') as mysqlvars_file:
                csv_reader = csv.reader(mysqlvars_file)
                for _, row in enumerate(csv_reader):
                    user_var = row[0]
                    pass_var = row[1]
                    host_var = row[2]
                    database_var = row[3]
            
            if class_pointer.current_connection == None:
                class_pointer.current_connection = mysql.connector.connect(user=user_var, password=pass_var, host=host_var, database=database_var)
            
        except IOError as error:
            print(f"(I/O Error): {error.strerror}")
            print("Please make sure that the .csv file exists.")
            return
        except mysql.connector.Error as msql_error:
            print(f"(Error connecting to database): {msql_error.msg}")
            logging.warning('Connection to MySQL failed, please make sure .csv file exists in config folder.')
            if class_pointer.current_connection != None:
                class_pointer.current_connection.close()
                class_pointer.current_connection = None
            return

        return class_pointer.current_connection        

    @classmethod
    def close_connection(class_pointer) -> bool:
        class_pointer.current_connection.commit()
        class_pointer.current_cursor.close()
        class_pointer.current_connection.close()
        logging.info("Database connection closed. Changes commited.")
        return True
    