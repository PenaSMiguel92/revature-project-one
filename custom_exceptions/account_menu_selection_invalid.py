class AccountMenuSelectionInvalid(Exception):
    """
        Thrown when user input is invalid, must be a menu option.
    """
    def __init__(self, message: str) -> None:
        self.message = '(Account Menu Selection Invalid) : ' + message