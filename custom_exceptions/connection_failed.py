import logging
class ConnectionFailed(Exception):
    """
        Thrown when connection to database fails because the appropriate .csv file is either missing or contains invalid values.
    """
    def __init__(self, message: str) -> None:
        logging.basicConfig(filename="logs/rxbuddy_database.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        self.message = '(Connection Failed) : ' + message
        logging.warning(self.message)