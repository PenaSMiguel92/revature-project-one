import logging
class BalanceInvalid(Exception):
    """
        Thrown when balance input is invalid.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Balance Invalid) : ' + message
        logging.warning(self.message)