from interface.data_access_object_interface import DataAccessObjectInterface
from data_model_classes.medication import Medication

class MedicationDAO(DataAccessObjectInterface):
    """
        This class is meant for retrieving medications from the medications table. 

        The medications table will be read-only.
    """
    def __init__(self):
        self.medications: list[Medication] = []
    
    def get_all_medications(self) -> bool:
        """
            This method will return all medications from the medications table.
            
            This method should only be accessible by an admin or doctor.

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass

    def get_medication_by_name(self, name: str) -> bool:
        """
            This method will return medication associated with provided name. 

            This method should be accessible from the prescription submenu. 

            This method will return a boolean True value if transaction was successful, raise an exception otherwise.
        """
        pass
    
