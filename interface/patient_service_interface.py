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
    def view_orders(self) -> None:
        ...
    
    @abstractmethod
    def delete_order(self) -> None:
        ...
    
    @abstractmethod
    def create_order(self) -> None:
        ...
    
    @abstractmethod
    def edit_order(self) -> None:
        ...

    @abstractmethod
    def view_prescriptions(self) -> None:
        ...