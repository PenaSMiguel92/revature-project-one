from interface.data_access_object_interface import DataAccessObjectInterface
from data_model_classes.shop_order import Shop_Order

class OrdersDAO(DataAccessObjectInterface):
    def __init__(self):
        self.orders = []
        
    def get_all_orders(self) -> bool:
        """
            This method will cache all orders from the orders table to a list.
            
            This method should only be accessible by an admin, and run only once per session.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def get_orders_by_username(self, username: str) -> list[Shop_Order]:
        """
            This method will return orders associated with provided username. 

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def create_order(self, order: Shop_Order) -> bool:
        """
            This method will insert specified order into orders table for saving.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def delete_order_by_id(self, order_id: int) -> bool:
        """
            This method will delete an order with the specified id.

            This method can be used to cancel an order, and the user's money will be returned.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass