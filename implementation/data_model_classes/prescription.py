from dataclasses import dataclass

@dataclass
class Prescription():
    """
        This data class will be used to model prescriptions gathered from joining accounts, medications, and prescriptions tables. 

        Information can be displayed to patients, doctors, and admins. 
    """
    prescriptionID: int
    prescribedBy: str
    prescribedTo: str
    medicationName: str
