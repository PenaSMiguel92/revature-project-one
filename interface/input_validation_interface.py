
#ABC -> Abstract Base Class

class InputValidation():

    @staticmethod
    def validate_input(input_value: str, **kwargs: any) -> bool:
        """
            This is a static method that can be inherited by any class that needs to validate input. It could've just been 
            a static class, but too late to change now.

            :params: Caller must provide the input value along with keyword arguments: char_input, integer_input, or string_input set to True,
            and if char_input, then provide a string containing valid characters as valid_input.
            :return: Returns a boolean value, true if valid input, false if not valid.
        """
        if kwargs.get('char_input') != None:
            return len(input_value) == 1 and input_value in kwargs['valid_input']
        elif kwargs.get('integer_input') != None:
            return input_value.isdigit()
        elif kwargs.get('string_input') != None:
            return input_value.isalpha() and len(input_value) > 2
        else:
            return False