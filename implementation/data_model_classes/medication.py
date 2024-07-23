from dataclasses import dataclass

@dataclass
class Medication():
    medication_id: int
    medication_price: float
    medication_name: str
    medication_description: str
