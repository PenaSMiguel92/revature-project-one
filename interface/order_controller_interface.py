from abc import abstractmethod
from interface.menu_baseclass import MenuBaseClass

class OrderServiceInterface(MenuBaseClass):
    @abstractmethod
    def set_state(self, state_value: int) -> None:
        pass

    @abstractmethod
    def get_state(self) -> int:
        pass
    
    @abstractmethod
    def view_orders(self) -> None:
        pass
    
    @abstractmethod
    def delete_order(self) -> None:
        pass
    
    @abstractmethod
    def create_order(self) -> None:
        pass
    
    @abstractmethod
    def edit_order(self) -> None:
        pass