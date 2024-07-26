from interface.data_access_object_interface import DataAccessObjectInterface
from data_model_classes.shop_order import Shop_Order
import logging

import mysql.connector
from mysql.connector.cursor import MySQLCursor

class OrdersDAO(DataAccessObjectInterface):
    def __init__(self):
        self.orders: list[Shop_Order] = []
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        
    def get_all_orders(self) -> list[Shop_Order]:
        """
            This method will cache all orders from the orders table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a list of Shop_Order ORM objects if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query = 'SELECT * FROM orders;'
        cursor.execute(query)
        self.orders = []
        for _, row in enumerate(cursor):
            self.orders.append(Shop_Order(int(row[0]), int(row[1]), int(row[2]), int(row[3]), float(row[4])))

        logging.info('All orders were retrieved successfully.')
        return self.orders

    def get_orders_by_username(self, username: str) -> list[Shop_Order]:
        """
            This method will return orders associated with provided username. 

            This method will return a list of Shop_Order ORM objects if transaction was successful, raise an exception otherwise.
        """
        cursor: MySQLCursor = super().get_cursor()
        query = f"SELECT o.orderID, o.accountID, o.medicationID, o.quantity, o.total_sales FROM accounts AS a JOIN orders AS o ON a.accountID = o.accountID WHERE a.accountUsername = \'{username}\'"
        cursor.execute(query)
        orders: list[Shop_Order] = []
        for _, row in enumerate(cursor):
            orders.append(Shop_Order(int(row[0]), int(row[1]), int(row[2]), int(row[3]), float(row[4])))

        logging.info(f'All orders by {username} were retrieved successfully.')
        return orders
    def create_order(self, order: Shop_Order) -> bool:
        """
            This method will insert specified order into orders table for saving.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        ...

    def update_order(self, order: Shop_Order) -> bool:
        ...

    def delete_order_by_id(self, order_id: int) -> bool:
        """
            This method will delete an order with the specified id.

            This method can be used to cancel an order, and the user's money will be returned.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        ...