import logging
class OrderInvalid(Exception):
    """
        Thrown when order id is invalid.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Order Invalid) : ' + message
        logging.warning(self.message)