from interface.data_access_object_interface import DataAccessObjectInterface

class AccountDAO(DataAccessObjectInterface):
    def __init__(self):
        self.accounts = []
             