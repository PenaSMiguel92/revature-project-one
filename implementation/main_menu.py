from interface.input_validation_interface import InputValidation
from interface.menu_interface import MenuInterface
from custom_exceptions.menu_selection_invalid import MenuSelectionInvalidException
# from custom_exceptions.invalid_profile import InvalidProfileException
# from custom_exceptions.data_missing import DataMissingException
# from implementation.profile_handler import ProfileHandler
# from implementation.biostat_handler import BiostatHandler

from implementation.account_service import AccountService

from enum import Enum

menu_state = Enum('MENU_STATE', [
'INITIAL_STATE',
'WAITING_STATE',
'ACCOUNT_SUBMENU_STATE',
'ADMIN_SUBMENU_STATE',
'ORDER_SUBMENU_STATE',
'PRESCRIPTION_SUBMENU_STATE',
'CLOSING_STATE'
])

class MainMenu(InputValidation, MenuInterface):
    """
        This class will handle the main command line interface (CLI). 
        
        It is a state machine dependent on user input. 
        
        The default state will be initial_state, and depending on user input the current_state will update accordingly. 

        I broke this logic down further into more classes to follow SOLID principles.
    """

    def __init__(self):
        self.current_state = menu_state.INITIAL_STATE
        self.account_service = None
        self.current_account = None
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
    
    def account_submenu(self) -> None:
        if self.account_service == None:
            self.account_service = AccountService()
        
        if not self.account_service.run():
            self.reset_state()

    def admin_submenu(self) -> None:
        return super().admin_submenu()
    
    def order_submenu(self) -> None:
        return super().order_submenu()
    
    def prescription_submenu(self) -> None:
        return super().prescription_submenu()
    
    # def reset_data(self) -> None:
    #     self.current_profile = None
    #     self.current_biostatHandler = None

    def display(self) -> None:
        print('\nWelcome to RXBuddy!')
        print('Please login or register...')
        self.current_state = menu_state.ACCOUNT_SUBMENU_STATE
        # print('(C)lose the application')
        # user_input = input().upper()
        # if not self.validate_input(user_input, char_input = True, valid_input = 'CLSRK'):
        #     raise MenuSelectionInvalidException("Please enter a valid menu option.")
        
        # match user_input:
        #     case 'C':
        #         self.current_state = menu_state.CREATING_PROFILE_STATE
        #     case 'L':
        #         self.current_state = menu_state.LOADING_PROFILE_STATE
        #     case 'S':
        #         self.current_state = menu_state.SHOW_HISTORY_STATE
        #     case 'R':
        #         self.current_state = menu_state.REPORT_BIOSTATS_STATE
        #     case 'K':
        #         self.current_state = menu_state.CLOSING_STATE
        #     case _:
        #         self.current_state = menu_state.INITIAL_STATE
    
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
        match self.current_state:
            case menu_state.INITIAL_STATE:
                self.display()
            case menu_state.ACCOUNT_SUBMENU_STATE:
                self.account_submenu()
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
            
