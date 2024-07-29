from dataclasses import dataclass

@dataclass
class Shop_Order():
    """
        This data class will be used to model shop_orders by joining the accounts, medications, and orders tables.

        The information can be displayed to patients and admins. 
    """
    orderID: int
    firstName: str
    lastName: str
    medicationName: str
    medicationCost: float
    quantity: int
    totalAmount: float
    