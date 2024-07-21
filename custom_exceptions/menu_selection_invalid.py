class MenuSelectionInvalidException(Exception):
    """
        Thrown when user input is not within a set of options 'CLRSK'. 
    """
    def __init__(self, message: str) -> None:
        self.message = "(Invalid Menu Selection) : " + message