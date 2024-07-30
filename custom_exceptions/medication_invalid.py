import logging
class MedicationInvalid(Exception):
    """
        Thrown when medication id, name or cost input is invalid.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Medication Invalid) : ' + message
        logging.warning(self.message)