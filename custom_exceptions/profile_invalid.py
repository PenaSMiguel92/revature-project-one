import logging
class ProfileInvalid(Exception):
    """
        Thrown when first or last name input is invalid.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Profile Invalid) : ' + message
        logging.warning(self.message)