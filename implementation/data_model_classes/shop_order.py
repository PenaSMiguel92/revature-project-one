from dataclasses import dataclass

@dataclass
class Shop_Order():
    """
        This data class will be used to model orders from the order table. 
    """
    orderID: int
    accountID: int
    medicationID: int
    quantity: int
    total_sales: float
    