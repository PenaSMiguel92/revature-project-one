from dataclasses import dataclass

@dataclass
class Shop_Order():
    """
        This data class will be used to model orders from the order table. 
    """
    order_id: int
    account_id: int
    medication_id: int
    order_total: float
    