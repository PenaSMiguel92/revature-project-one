from abc import ABC, abstractmethod

class MenuBaseClass(ABC):
    @abstractmethod
    def display(self) -> None:
        """
            This method will display the menu, and through polymorphism, the functionality will vary.
        """
        pass

    @abstractmethod
    def run(self) -> None:
        """
            This method will execute depending on the current state, and through polymorphism, the functionality will vary.
        """
        pass