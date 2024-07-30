from interface.patient_service_interface import PatientServiceInterface
from interface.input_validation_interface import InputValidation

from implementation.data_access_classes.prescription_dao import PrescriptionDAO
from implementation.data_access_classes.orders_dao import OrdersDAO

from implementation.data_model_classes.account import Account
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.prescription import Prescription
from implementation.data_model_classes.shop_order import Shop_Order

from custom_exceptions.patient_menu_selection_invalid import PatientMenuSelectionInvalid

from enum import Enum

patient_service_state = Enum('PATIENT_STATE', [
    'INITIAL_STATE',
    'PRESCRIPTIONS_STATE',
    'ORDERS_STATE',
    'CLOSING_STATE'
])

class PatientService(InputValidation, PatientServiceInterface):
    def __init__(self, current_account: Account):
        self.current_state = patient_service_state.INITIAL_STATE
        self.prescriptions_dao: PrescriptionDAO = PrescriptionDAO()
        self.orders_dao: OrdersDAO = OrdersDAO()

        self.prescriptions: list[Prescription] = self.prescriptions_dao.get_prescriptions_by_patientID(current_account.accountID)
        self.orders: list[Shop_Order] = self.orders_dao.get_orders_by_username(current_account.accountUsername)

        self.current_account = current_account
     
    def set_state(self, state_value: int) -> None:
        self.current_state = state_value
    
    def get_state(self) -> int:
        return self.current_state
    
    def process_input(self, input: str) -> None:
        match (input):
            case 'A':
                self.current_state = patient_service_state.PRESCRIPTIONS_STATE
            case 'B':
                self.current_state = patient_service_state.ORDERS_STATE
            case 'C':
                self.current_state = patient_service_state.CLOSING_STATE

    def display_orders(self) -> bool:
        ...
    
    
    def display_prescriptions(self) -> bool:
        ...

    
    def logoff(self) -> None:
        self.prescriptions_dao.close_connection()
        self.orders_dao.close_connection()
        

        
    def display(self) -> bool:
        print('\nWould you like to make or modify an order? ')
        print('A. Make an order.')
        print('B. Modify an order.')
        print('C. Sign out.')
        while self.current_state == patient_service_state.INITIAL_STATE:
            try:
                user_input = input('>>>').upper()
                if not self.validate_input(user_input, char_input = True, valid_input = 'ABC'):
                    raise PatientMenuSelectionInvalid("Please choose a valid menu option.")
                self.process_input(user_input)
            except PatientMenuSelectionInvalid as err:
                print(err.message) #note logging is handled when exception is created.

        return True
    
    def run(self) -> bool:
        match self.current_state:
            case patient_service_state.INITIAL_STATE:
                return self.display()
            case patient_service_state.PRESCRIPTIONS_STATE:
                return self.display_prescriptions()
            case patient_service_state.ORDERS_STATE:
                return self.display_orders()
            case patient_service_state.CLOSING_STATE:
                return True