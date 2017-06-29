class UserInput:
    """
    Creates UserInput object.
    """

    def get_option(self, options):
        """
        Returns the option from the options list depeding on the user input.
        Parameters:
        options: list

        Returns:
        options[user_decision - 1]: str
        """

        user_input_number = None
        while user_input_number not in range(len(options)):
            user_input_number = int(input("\nPick an option (number): "))

        user_decision = options[user_input_number - 1]
        return user_decision


    
