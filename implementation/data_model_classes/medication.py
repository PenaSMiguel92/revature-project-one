from dataclasses import dataclass

@dataclass
class Medication():
    """
        This data class will be used to model medications gathered from the medications table. 

        Information can be displayed to patients (when prescribed), doctors, and admins. 
    """
    medicationID: int
    medicationName: str
    medicationCost: float
   
