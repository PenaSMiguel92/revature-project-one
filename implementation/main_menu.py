from interface.input_validation import InputValidation
from interface.menu_interface import MenuInterface
from custom_exceptions.menu_selection_invalid import MenuSelectionInvalidException
# from custom_exceptions.invalid_profile import InvalidProfileException
# from custom_exceptions.data_missing import DataMissingException
# from implementation.profile_handler import ProfileHandler
# from implementation.biostat_handler import BiostatHandler
from enum import Enum

menu_state = Enum('MENU_STATE', [
'INITIAL_STATE',
'WAITING_STATE',
'CREATING_USER_STATE',
'LOADING_USER_STATE',
'DELETING_USER_STATE',
'SETTING_USER_ROLE_STATE',
'SHOW_ADMINMENU_STATE',
'SHOWING_USERS_STATE',
'SHOWING_ORDERS_STATE',
'CREATE_ORDER_STATE',
'DELETE_ORDER_STATE',
'CLOSING_STATE'
])

class MainMenu(InputValidation, MenuInterface):
    """
        This class will handle the main command line interface (CLI). 
        
        It is a state machine dependent on user input. 
        
        The default state will be initial_state, and depending on user input the current_state will update accordingly. 

        I can break this logic down further into more classes to follow SOLID principles, but that is beyond the scope of this project.
    """

    def __init__(self):
        self.current_state = menu_state.INITIAL_STATE
        # self.current_profile = None
        # self.current_biostatHandler = None
    
    def set_state(self, state_value: int) -> None:
        self.current_state = state_value
    
    def get_state(self) -> int:
        return self.current_state
    
    def reset_state(self) -> None:
        """
            This is an encapsulated method that should only be accessible by this class.

            There's only so much DRY can do, I still need to call this method at the end of every menu option method.
        """
        self.current_state = menu_state.INITIAL_STATE
    
    # def reset_data(self) -> None:
    #     self.current_profile = None
    #     self.current_biostatHandler = None

    def display_menu(self) -> None:
        print('\nWelcome to RXBuddy!')
        print('What would you like to do?')
        print('(C)reate profile') 
        print('(L)oad profile') 
        print('(S)how history') 
        print('(R)eport BGC and BMI')
        print('(K)lose the application') #Mortal Kombat spelling, since C was already taken.
        user_input = input().upper()
        if not self.validate_input(user_input, char_input = True, valid_input = 'CLSRK'):
            raise MenuSelectionInvalidException("Please enter a valid menu option.")
        
        match user_input:
            case 'C':
                self.current_state = menu_state.CREATING_PROFILE_STATE
            case 'L':
                self.current_state = menu_state.LOADING_PROFILE_STATE
            case 'S':
                self.current_state = menu_state.SHOW_HISTORY_STATE
            case 'R':
                self.current_state = menu_state.REPORT_BIOSTATS_STATE
            case 'K':
                self.current_state = menu_state.CLOSING_STATE
            case _:
                self.current_state = menu_state.INITIAL_STATE
    
    def create_profile(self) -> None:
        pass
        # self.reset_state()
        # self.reset_data()
        # profile_handler: ProfileHandler = ProfileHandler()
        # if profile_handler.create_profile():
        #     self.current_profile = profile_handler
            
    def load_profile(self) -> None:
        pass
        # self.reset_state()
        # self.reset_data()
        # profile_handler: ProfileHandler = ProfileHandler()
        # if profile_handler.load_profile():
        #     self.current_profile = profile_handler

    def load_data(self) -> None:    
        pass
        # if self.current_profile == None:
        #     self.reset_state()
        #     raise InvalidProfileException("You haven't created or loaded a profile yet.")
        
        # filename = self.current_profile.get_filename()
        # const_biostats: list[int] = self.current_profile.get_const_biostats()

        # biostat_handler: BiostatHandler = BiostatHandler()
        # if biostat_handler.load_data(filename, const_biostats):
        #     self.current_biostatHandler = biostat_handler

    def show_history(self) -> None:
        pass
        # self.reset_state()
        # if self.current_biostatHandler == None:
        #     raise DataMissingException('Data is missing, please either report some data or load a profile.')
        
        # self.current_biostatHandler.show_data()

    def report_biostats(self) -> None:
        pass
        # self.reset_state()
        # if self.current_biostatHandler != None:
        #     self.current_biostatHandler.append_data()
        #     return
        
        # biostat_handler: BiostatHandler = BiostatHandler()
        # if biostat_handler.create_data():
        #     self.current_biostatHandler = biostat_handler
        

    def run(self) -> None:
        pass
        # match self.current_state:
        #     case menu_state.INITIAL_STATE:
        #         self.display_menu()
        #     case menu_state.CREATING_PROFILE_STATE:
        #         self.create_profile()
        #     case menu_state.LOADING_PROFILE_STATE:
        #         self.load_profile()
        #     case menu_state.SHOW_HISTORY_STATE:
        #         if self.current_biostatHandler == None: 
        #             self.load_data()

        #         self.show_history()
        #     case menu_state.REPORT_BIOSTATS_STATE:
        #         if self.current_biostatHandler == None:
        #             self.load_data()
                
        #         self.report_biostats()
        #         if self.current_biostatHandler != None and self.current_profile != None:
        #             filename = self.current_profile.get_filename()
        #             self.current_biostatHandler.save_data(filename)
        #     case _: #The only other state it can be is menu_state.CLOSING_STATE
        #         print("Closing tracker. Have a nice day :)") 
            
