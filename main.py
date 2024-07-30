from custom_exceptions.menu_selection_invalid import MenuSelectionInvalidException
# from custom_exceptions.invalid_history_selection import InvalidHistorySelectionException
# from custom_exceptions.invalid_profile import InvalidProfileException
# from custom_exceptions.invalid_bgc import InvalidBGCException
# from custom_exceptions.invalid_bmi import InvalidBMIException
# from custom_exceptions.data_missing import DataMissingException
from implementation.main_menu import MainMenu, menu_state

def main() -> None:
    """
        Program entry point, should handle exceptions at the highest level, and run the menu logic as needed.

    """
    menu_object: MainMenu = MainMenu()

    while menu_object.get_state() != menu_state.CLOSING_STATE:
        try:
            menu_object.run()
        except (MenuSelectionInvalidException) as e:
            print(e.message)
    menu_object.close_connections()
    print("Closing RxBuddy... Have a nice day :)")
if __name__ == "__main__":
    main()