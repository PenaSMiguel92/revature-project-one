import logging
class DoctorMenuSelectionInvalid(Exception):
    """
        Thrown when user input is invalid, must be a valid submenu option.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Doctor Menu Selection Invalid) : ' + message
        logging.warning(self.message)