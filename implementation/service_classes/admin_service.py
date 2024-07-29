from interface.admin_service_interface import AdminServiceInterface
from interface.input_validation_interface import InputValidation

from implementation.data_access_classes.account_dao import AccountDAO
from implementation.data_access_classes.medication_dao import MedicationDAO
from implementation.data_access_classes.orders_dao import OrdersDAO

from implementation.data_model_classes.account import Account
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.shop_order import Shop_Order


class AdminService(InputValidation, AdminServiceInterface):
    def __init__(self, current_account):
        # self.account_dao: AccountDAO = AccountDAO.get
        self.medications: list[Medication] = []
        self.shop_orders: list[Shop_Order] = []
        self.current_account = current_account

    