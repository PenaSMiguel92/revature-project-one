from interface.data_access_object_interface import DataAccessObjectInterface
from implementation.data_model_classes.account import Account
from implementation.data_access_classes.account_dao import AccountDAO
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.shop_order import Shop_Order
import logging

import mysql.connector
from mysql.connector.cursor import MySQLCursor

class OrdersDAO(DataAccessObjectInterface):
    def __init__(self):
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        
    def get_all_orders(self) -> list[Shop_Order]:
        """
            This method will cache all orders from the orders table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a list of Shop_Order ORM objects if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query_start = 'SELECT o.orderID, a.accountUsername, a.firstName, a.lastName, m.medicationName, m.medicationCost, o.quantity, o.totalAmount '
        query_joining = 'FROM orders AS o JOIN accounts AS a ON o.accountID=a.accountID JOIN medications AS m ON o.medicationID=m.medicationID;'
        cursor.execute(query_start + query_joining)
        orders: list[Shop_Order] = [Shop_Order(int(row[0]), row[1], row[2], row[3], row[4], float(row[5]), int(row[6]), float(row[7])) for _, row in enumerate(cursor)]

        logging.info('All orders were retrieved successfully.')
        return orders

    def get_orders_by_username(self, username: str) -> list[Shop_Order]:
        """
            This method will return orders associated with provided username. 

            This method will return a list of Shop_Order ORM objects if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query_returnColumns = 'SELECT o.orderID, a.accountUsername, a.firstName, a.lastName, m.medicationName, m.medicationCost, o.quantity, o.totalAmount ' 
        query_joining = f'FROM orders AS o JOIN accounts AS a ON o.accountID=a.accountID JOIN medications AS m ON o.medicationID=m.medicationID '
        query_condition = f'WHERE a.accountUsername=\'{username}\';'
        cursor.execute(query_returnColumns + query_joining + query_condition)
        orders_by_username: list[Shop_Order] = [Shop_Order(int(row[0]), row[1], row[2], row[3], row[4], float(row[5]), int(row[6]), float(row[7])) for _, row in enumerate(cursor)]

        logging.info(f'All orders by {username} were retrieved successfully.')
        return orders_by_username
    
    def get_order_by_id(self, order_id: int) -> Shop_Order:
        """
            This method will return one order associated with the specified order_id.
        """
        cursor: MySQLCursor = super().get_cursor()
        query_returnColumns = 'SELECT o.orderID, a.accountUsername, a.firstName, a.lastName, m.medicationName, m.medicationCost, o.quantity, o.totalAmount ' 
        query_joining = f'FROM orders AS o JOIN accounts AS a ON o.accountID=a.accountID JOIN medications AS m ON o.medicationID=m.medicationID '
        query_condition = f'WHERE o.orderID={order_id};'
        cursor.execute(query_returnColumns + query_joining + query_condition)
        for _, row in enumerate(cursor):
            order: Shop_Order = Shop_Order(int(row[0]), row[1], row[2], row[3], row[4], float(row[5]), int(row[6]), float(row[7]))
            break

        logging.info(f'The order with ID: {order_id} was retrieved successfully.')
        return order
    
    def create_order(self, patient: Account, medication: Medication, quantity: int) -> bool:
        """
            This method will create an order and insert it into orders table for saving based on the patient account object and medication object and how much was purchased.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query_start = 'INSERT INTO orders (orderID, accountID, medicationID, quantity, totalAmount) VALUES '
        query_mid = f'(DEFAULT, {patient.accountID}, {medication.medicationID}, {quantity}, '
        query_end = '{:.2f});'.format(quantity * medication.medicationCost)
        cursor.execute(query_start + query_mid + query_end)

        super().commit_changes()
        logging.info(f'Created order for {patient.accountUsername} and saved to database.')
        return True

    def delete_order_by_id(self, order_id: int) -> bool:
        """
            This method will delete an order with the specified id.

            This method can be used to cancel an order, and the user's money will be returned.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        try:
            cursor: MySQLCursor = super().get_cursor()
            order: Shop_Order = self.get_order_by_id(order_id)

            account_dao: AccountDAO = AccountDAO()

            patient: Account = account_dao.get_account_by_username(order.username)
            patient.balance += order.totalAmount
            account_dao.update_account(patient)
            query = f'DELETE FROM orders WHERE orderID={order_id}'
            cursor.execute(query)
        except mysql.connector.Error as Err:
            print('Please make sure that the order id is valid.')
            logging.error(Err.msg)
            return False
        
        super().commit_changes()
        logging.info(f'Deleted order with ID: {order_id} from orders table and refunded ${order.totalAmount} to {patient.accountUsername} in database.')
        return True  