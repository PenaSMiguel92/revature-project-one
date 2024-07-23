from dataclasses import dataclass

@dataclass
class Medication():
    """
        This data class will be used to model medications gathered from the medications table. 

        Information can be displayed to patients, doctors, and admins. 
    """
    medication_id: int
    medication_price: float
    medication_name: str
    medication_description: str
