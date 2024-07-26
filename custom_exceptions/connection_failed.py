class ConnectionFailed(Exception):
    """
        Thrown when connection to database fails because the appropriate .csv file is either missing or contains invalid values.
    """
    def __init__(self, message: str) -> None:
        self.message = '(Connection Failed) : ' + message