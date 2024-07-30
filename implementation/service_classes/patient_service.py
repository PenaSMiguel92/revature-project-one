from interface.patient_service_interface import PatientServiceInterface
from interface.input_validation_interface import InputValidation

from implementation.data_access_classes.prescription_dao import PrescriptionDAO
from implementation.data_access_classes.orders_dao import OrdersDAO

from implementation.data_model_classes.account import Account
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.prescription import Prescription
from implementation.data_model_classes.shop_order import Shop_Order

from enum import Enum

patient_service_state = Enum('PATIENT_STATE', [
    'INITIAL_STATE',
    'PRESCRIPTIONS_STATE',
    'ORDERS_STATE',
    'CLOSING_STATE'
])

class PatientService(InputValidation, DoctorServiceInterface):
    def __init__(self, current_account: Account):
        self.prescriptions_dao: PrescriptionDAO = PrescriptionDAO()
        self.orders_dao: OrdersDAO = OrdersDAO()

        self.prescriptions: list[Prescription] = self.prescriptions_dao.get_prescriptions_by_patientID(current_account.accountID)
        self.orders: list[Shop_Order] = self.orders_dao.get_orders_by_username(current_account.accountUsername)

        self.current_account = current_account
    
     
    def set_state(self, state_value: int) -> None:
        ...

    
    def get_state(self) -> int:
        ...
    
    
    def display_orders(self) -> None:
        ...
    
    
    def display_prescriptions(self) -> None:
        ...

    
    def logoff(self) -> None:
        ...

        
    def display(self) -> None:
        ...

    
    def run(self) -> None:
        ...