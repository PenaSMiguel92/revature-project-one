from abc import abstractmethod
from interface.menu_baseclass import MenuBaseClass

class PatientServiceInterface(MenuBaseClass):
    @abstractmethod
    def set_state(self, state_value: int) -> None:
        ...

    @abstractmethod
    def get_state(self) -> int:
        ...
    
    @abstractmethod
    def view_prescriptions_by_patientID(self) -> None:
        ...
    
    @abstractmethod
    def delete_prescription(self) -> None:
        ...
    
    @abstractmethod
    def create_prescription(self) -> None:
        ...
    
    @abstractmethod
    def edit_prescription(self) -> None:
        ...

    @abstractmethod
    def view_all_prescriptions(self) -> None:
        ...