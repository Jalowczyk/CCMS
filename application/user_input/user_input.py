import getpass
import re


class UserInput:
    """
    Creates UserInput object.
    """
    def __init__(self, view):
        self.view = view

    def get_option(self, options):
        """
        Returns the option from the options list depending on the user input.
        Parameters:
        options: list

        Returns:
        user_decision: str
        """

        user_input_number = input("\nPick an option (number): ")
        while not user_input_number.isnumeric() or int(user_input_number) not in range(1, len(options) + 1):
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_number = input("\nPick an option (number): ")
        user_decision = options[int(user_input_number) - 1]
        return user_decision

    def get_boolean_input(self):
        """
        Return boolean depending on the user input.

        Returns:
        boolean: True/False
        """

        user_input_bool = input("\nPick an option (y/n): ").lower()
        while user_input_bool not in ["y", "n"]:
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_bool = input("\nPick an option (y/n): ").lower()

        if user_input_bool == "y":
            return True
        else:
            return False

    def get_login_input(self):
        """
        Returns email and password depending on user input.

        Returns:
        user_input_email: str
        user_input_password: str
        """

        user_input_email = input("Enter your email: ")
        while not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_input_email):
            self.view.show_message("Wrong mail.")
            user_input_email = input("Enter your email: ")

        user_input_password = getpass.getpass("Enter your password: ")
        while not user_input_password:
            user_input_password = getpass.getpass("Enter your password: ")

        return user_input_email, user_input_password

    def get_assignment_data(self):
        """
        Returns assignment title, desctiption od maximum grade depending on user input.

        Returns:
        user_assignment_title: str
        user_assignment_description: str
        user_assignment_max_grade: int
        """

        user_assignment_title = input("Enter assignment title: ")
        while not user_assignment_title:
            self.view.show_message("This field can't be empty.")
            user_assignment_title = input("Enter assignment title: ")

        user_assignment_description = input("Enter assignment description: ")

        user_assignment_max_grade = input("Enter assignment maximum grade: ")
        while not user_assignment_max_grade.isnumeric() or int(user_assignment_max_grade) <= 0:
            self.view.show_message("Sorry, your input is incorrect.")
            user_assignment_max_grade = input("Enter assignment maximum grade: ")

        return user_assignment_title, user_assignment_description, int(user_assignment_max_grade)

    def get_index_input(self, list_length):
        """
        Returns index depending on user input.

        Returns:
        user_input_index: int
        """

        user_input_index = input("Pick a number: ")
        while not user_input_index.isnumeric() or int(user_input_index) not in range(1, list_length + 1):
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_index = input("Pick a number: ")

        return int(user_input_index) - 1

    def get_codecooler_data(self):
        """
        Returns codecooler first name, last name and email depending on user input.

        Returns:
        codecooler_first_name: str
        codecooler_second_name: str
        codecooler_email: str
        """

        codecooler_first_name = input("Enter first name: ")
        while not codecooler_first_name:
            self.view.show_message("This field can't be empty.")
            codecooler_first_name = input("Enter first name: ")

        codecooler_second_name = input("Enter second name: ")
        while not codecooler_second_name:
            self.view.show_message("This field can't be empty.")
            codecooler_second_name = input("Enter second name: ")

        codecooler_email = input("Enter email: ")
        while not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", codecooler_email):
            self.view.show_message(("Wrong e-mail: e-mail can contain ")
            + ("following characters: letters, integers, '_', '.', '+', '-'."))
            codecooler_email = input("Enter email: ")

        codecooler_password = input("Enter password: ")
        while not codecooler_password:
            self.view.show_message("This field can't be empty.")
            codecooler_password = input("Enter password: ")

        return codecooler_first_name, codecooler_second_name, codecooler_email, codecooler_password

    def get_grade_input(self, submission):
        """
        Returns grade integer depending on user input.

        Returns:
        user_input_grade: int
        """

        user_input_grade = input("Enter a grade: ")
        while not user_input_grade.isnumeric() or int(user_input_grade) not in range(
                        submission.get_assignment().get_max_grade() + 1):
            self.view.show_message("\nSorry, your input is incorrect.\n")
            user_input_grade = input("Enter a number: ")

        return int(user_input_grade)

    def get_numeric_input(self):
        """
        Returns integer depending on user input.

        Returns:
        user_input_number: int
        """

        user_input_number = input("Enter a number: ")
        while not user_input_number.isnumeric():
            self.view.show_message("\nSorry, your input is incorrect.\n")
            user_input_number = input("Enter a number: ")

        return int(user_input_number)

    def get_text_input(self):
        """
        Returns str depending on user input.

        Returns:
        user_input_text: str
        """

        user_input_text = input("Type here: ")

        return user_input_text
