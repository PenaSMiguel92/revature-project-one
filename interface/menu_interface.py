from abc import ABC, abstractmethod

class MenuInterface(ABC):

    @abstractmethod
    def set_state(self, state_value: int) -> None:
        """
            Encapsulation method for setting the current state of the menu object.

            :params: The enum menu_state holds the various valid program states.  
        """
        pass

    @abstractmethod
    def get_state(self) -> int:
        """
            Encapsulation method for getting the current state of the menu object.

            :params:
            :return: This will be an int associated with the enum menu_state
        """
        pass

    @abstractmethod
    def display_menu(self) -> None:
        """
            Method for displaying menu options and listening for user input.

        """
        pass

    @abstractmethod
    def create_profile(self) -> None:
        """
            Method for creating a 'profile' which is just a file containing BGC and BMI data.
            
            Raises a invalid profile exception whenever the user inputs a name that is too short (< 3 chars), or if the file already exists.

            Logic is handled by a profile handler object.
        """
        pass
    
    @abstractmethod
    def load_profile(self) -> None:
        """
            Load a profile from a file by asking the user for their name. It will then load profile details accordingly.

            This method will not handle any exceptions thrown by the profile handler, since the goal is to have exception handling at the main loop.

            logic is handled by a profile handler object.
        """
        pass

    @abstractmethod
    def load_data(self) -> None:
        """
            This method should only succeed if there's a profile currently loaded, and data exists in the file.
        """
        pass
    @abstractmethod
    def show_history(self) -> None:
        """
            This method will use an existing profile handler object and load all rows of data saved so far. It will then plot the data with matplotlib.

            This method will raise an invalid profile exception if the profile object does not exist, and the user will need to create or load one. 

            Logic is handled by a data history object, which handles converting csv rows into respective BGC and BMI objects, which in turn are used to plot the data.
        """
        pass

    @abstractmethod
    def report_biostats(self) -> None: 
        """
            This method will use an existing profile handler object and ask it for the user's height before asking the user for their weight, and then creating a BMI object.
            It will then ask for the BGC and store it in a BGC object.

            This method will raise the respective invalid bgc and bmi exceptions if the user does not input a valid weight or BGC. 

            Logic is handled by a biostat handler object, which handles converting user input into respective BGC and BMI objects and then saving them to the profile.
        """
        pass

    @abstractmethod
    def run(self) -> None:
        """
            This method handles the main menu logic until the state becomes menu_state.CLOSING_STATE
            
            This method will raise the menuselectioninvalid exception if the user does not provide a valid input. 
        """
        pass