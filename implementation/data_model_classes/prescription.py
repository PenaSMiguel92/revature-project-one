from dataclasses import dataclass

@dataclass
class Prescription():
    prescriptionID: int
    prescribedBy: str
    prescribedTo: str
    medication: str
