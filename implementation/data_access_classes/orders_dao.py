from interface.data_access_object_interface import DataAccessObjectInterface

class OrdersDAO(DataAccessObjectInterface):
    def __init__(self):
        self.orders = []
        
