from interface.doctor_service_interface import DoctorServiceInterface
from interface.input_validation_interface import InputValidation

from implementation.data_access_classes.account_dao import AccountDAO
from implementation.data_access_classes.medication_dao import MedicationDAO
from implementation.data_access_classes.prescription_dao import PrescriptionDAO

from implementation.data_model_classes.account import Account
from implementation.data_model_classes.medication import Medication
from implementation.data_model_classes.prescription import Prescription

from enum import Enum

doctor_service_state = Enum('DOCTOR_STATE', [
    'INITIAL_STATE',
    'PATIENTS_STATE',
    'MEDICATIONS_STATE',
    'PRESCRIPTIONS_STATE',
    'CLOSING_STATE'
])

class DoctorService(InputValidation, DoctorServiceInterface):
    def __init__(self, current_account: Account):
        self.account_dao: AccountDAO = AccountDAO()
        self.medication_dao: MedicationDAO = MedicationDAO()
        self.prescriptions_dao: PrescriptionDAO = PrescriptionDAO()

        self.accounts: list[Account] = self.account_dao.get_all_patients()
        self.medications: list[Medication] = self.medication_dao.get_all_medications()
        self.prescriptions: list[Prescription] = self.prescriptions_dao.get_prescriptions_by_doctorID(current_account.accountID)

        self.current_account = current_account

     
    def set_state(self, state_value: int) -> None:
        ...

    
    def get_state(self) -> int:
        ...
    
    
    def display_prescriptions(self) -> None:
        
        ...

    
    def display_medications(self) -> None:
       
        ...
    
    
    def display_patients(self) -> None:
        
        ...

    
    def logoff(self) -> None:
        
        ...

        
    def display(self) -> None:
        
        ...

    
    def run(self) -> None:
       
        ...