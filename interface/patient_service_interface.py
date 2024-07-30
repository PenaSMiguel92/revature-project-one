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
    def display_orders(self) -> None:
        """
            Displays all orders by this patient, and provides an interface for orders.
        """
        ...
    
    @abstractmethod
    def display_prescriptions(self) -> None:
        """
            Displays all prescribed medications to this patient, and provides an interface for purchasing and creating orders.
        """
        ...

    @abstractmethod
    def logoff(self) -> None:
        """
            This method is called when user wants to logoff.
        """
        ...

    