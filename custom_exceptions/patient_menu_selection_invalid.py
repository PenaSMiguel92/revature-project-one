import logging
class PatientMenuSelectionInvalid(Exception):
    """
        Thrown when user input is invalid, must be a menu option.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Account Menu Selection Invalid) : ' + message
        logging.warning(self.message)