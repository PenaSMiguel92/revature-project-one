import logging
class MenuSelectionInvalidException(Exception):
    """
        Thrown when user input is not within a set of options 'CLRSK'. 
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = "(Invalid Menu Selection) : " + message
        logging.warning(self.message)