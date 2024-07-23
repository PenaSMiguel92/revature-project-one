from dataclasses import dataclass

@dataclass
class Shop_Order():
    order_id: int
    account_id: int
    medication_id: int
    order_total: float
    