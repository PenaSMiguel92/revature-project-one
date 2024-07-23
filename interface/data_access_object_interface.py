from abc import ABC
import csv
from mysql.connector import MySQLConnection

class DataAccessObjectInterface(ABC):

    current_connection: MySQLConnection = None

    @classmethod
    def get_connection(class_pointer) -> MySQLConnection:
        """
            Make sure to have a .csv file with user, password, host, and database columns in a directory called config/
        """
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
                class_pointer.current_connection = MySQLConnection(user=user_var, password=pass_var,
                              host=host_var, 
                              database=database_var)
        except IOError as error:
            print(f"(I/O Error): {error.strerror}")
            print("Please make sure that the .csv file exists.")
            return
        except Exception:
            print(f"(Unknown Exception): ")
            if class_pointer.current_connection != None:
                class_pointer.current_connection.close()
                class_pointer.current_connection = None
            return

        return class_pointer.current_connection        

    