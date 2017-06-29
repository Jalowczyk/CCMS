import getpass

class UserInput:
    """
    Creates UserInput object.
    """

    def get_option(self, options):
        """
        Returns the option from the options list depending on the user input.
        Parameters:
        options: list

        Returns:
        user_decision: str
        """

        user_input_number = int(input("\nPick an option (number): "))
        while user_input_number not in range(len(options)):
            user_input_number = int(input("\nPick an option (number): "))

        user_decision = options[user_input_number - 1]
        return user_decision

    def get_boolean_input(self):
        """
        Return boolean depending on the user input.

        Returns:
        boolean: True/False
        """

        user_input_bool = input("\nPick an option (y/n): ").lower()
        while user_input_bool not in ["y", "n"]:
            user_input_bool = input("\nPick an option (y/n): ").lower()

        if user_input_bool == "y":
            return True
        else:
            return False

    
