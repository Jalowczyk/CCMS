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

        user_input_number = input("\nEnter menu option: ")
        while not user_input_number.isnumeric() or int(user_input_number) not in range(1, len(options) + 1):
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_number = input("\nEnter menu option again: ")
        user_decision = options[int(user_input_number) - 1]
        return user_decision

    def get_boolean_input(self):
        """
        Return boolean depending on the user input.

        Returns:
        boolean: True/False
        """

        user_input_bool = input("\nEnter yes or no: ").lower()
        while user_input_bool not in ["y", "n", "yes", "no"]:
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_bool = input("\nEnter yes or no again: ").lower()

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
            self.view.show_message("Wrong email.")
            user_input_email = input("Enter your email (or '0', to go back): ")
            if user_input_email == '0':
                return None

        user_input_password = getpass.getpass("Enter your password: ")
        while not user_input_password:
            user_input_password = getpass.getpass("Enter your password (or press 'enter', to go back): ")
            if user_input_password == '':
                return None
        return user_input_email, user_input_password

    def get_assignment_data(self):
        """
        Returns assignment title, desctiption od maximum grade depending on user input.

        Returns:
        None:
            if user break action by enter.

        user_assignment_title: str
        user_assignment_description: str
        user_assignment_max_grade: int


        """

        user_assignment_title = input("\nEnter assignment title: ")
        while not user_assignment_title:
            self.view.show_message("This field can't be empty.")
            user_assignment_title = input("Enter assignment title again (or press enter to go back): ")
            if user_assignment_title == '':
                return

        user_assignment_description = input("Enter assignment description (or press enter to go back): ")
        if user_assignment_description == '':
            return

        user_assignment_max_grade = input("Enter assignment maximum grade (or press enter to go back): ")
        if user_assignment_max_grade == '':
            return
        while not user_assignment_max_grade.isnumeric() or int(user_assignment_max_grade) <= 0:
            self.view.show_message("Sorry, your input is incorrect.")
            user_assignment_max_grade = input("Enter assignment maximum grade again (or press enter to go back): ")
            if user_assignment_title == '':
                return

        return user_assignment_title, user_assignment_description, int(user_assignment_max_grade)

    def get_index_input(self, list_length, group_name):
        """
        Returns index depending on user input.

        Returns:
        user_input_index: int
        """

        user_input_index = input("\nEnter {} index: ".format(group_name))
        while not user_input_index.isnumeric() or int(user_input_index) not in range(1, list_length + 1):
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_index = input("Enter index again: ")

        return int(user_input_index) - 1

    def get_aux_menu_input(self, list_length, group_name):
        """
        Return index of thing which details user want to see, if
        user chose to see it.

        Returns:
        user_index_decision: int
        """
        options = ["show details", "back"]
        self.view.show_message("What do you want to do?")
        self.view.show_menu_option(options)
        user_decision = self.get_option(options)

        if user_decision == "show details":
            user_index_decision = self.get_index_input(list_length, group_name)
            return int(user_index_decision)

    def get_codecooler_email_input(self):
        """
        Returns codecooler e-mail depending on user input.


        Returns:
        codecooler_email: str

        or

        None
            If user decided to go back by press enter
        """
        codecooler_email = input("\nEnter new e-mail: ")

        while not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", codecooler_email):
            self.view.show_message(("Wrong e-mail: e-mail can contain ")
                                   + ("following characters: letters, integers, '_', '.', '+', '-'."))
            codecooler_email = input("Enter new e-mail again: (or press returrn to go back): ")
            if codecooler_email == '':
                None

        return codecooler_email

    def get_specific_codecooler_data(self, data_type):
        """
        Returns codecooler specific data depending on user input.

        Returns:
        codecooler_data: str
        """

        codecooler_data = input("\n{} {}: ".format("Enter new ", data_type))
        while not codecooler_data:
            self.view.show_message("This field can't be empty. Press enter if you want to dicard changes.")
            codecooler_data = input("{} {} {}: ".format("Enter new ", data_type, "again"))
            if codecooler_data == '':
                return
        return codecooler_data

    def get_codecooler_data(self):
        """
        Returns codecooler first name, last name and email depending on user input.

        Returns:
        None:
            If user go back by press enter

        codecooler_first_name: str
        codecooler_second_name: str
        codecooler_email: str
        """

        codecooler_first_name = input("\nEnter first name: ")
        while not codecooler_first_name:
            self.view.show_message("This field can't be empty.")
            codecooler_first_name = input("Enter first name again ('Or press enter to go back'): ")
            if codecooler_first_name == '':
                return

        codecooler_second_name = input("Enter second name: ")
        while not codecooler_second_name:
            self.view.show_message("This field can't be empty.")
            codecooler_second_name = input("Enter second name again ('Or press enter to go back'): ")
            if codecooler_second_name == '':
                return

        codecooler_email = input("Enter email: ")
        while not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", codecooler_email):
            self.view.show_message(("Wrong e-mail: e-mail can contain ")
                                   + ("following characters: letters, integers, '_', '.', '+', '-'."))
            codecooler_email = input("Enter email again ('Or press enter to go back'): ")
            if codecooler_email == '':
                return

        codecooler_password = input("Enter password ('Or press enter to go back'): ")
        if codecooler_password == '':
            return

        return codecooler_first_name, codecooler_second_name, codecooler_email, codecooler_password

    def get_grade_input(self, submission):
        """
        Returns grade integer depending on user input.

        Returns:
        user_input_grade: int
        """

        user_input_grade = input("\nEnter grade: ")
        while not user_input_grade.isnumeric() or int(user_input_grade) not in range(
                        submission.get_assignment().get_max_grade() + 1):
            self.view.show_message("Sorry, your input is incorrect.")
            user_input_grade = input("Enter grade again: ")

        return int(user_input_grade)

    def get_text_input(self):
        """
        Returns str depending on user input.

        Returns:
        user_input_text: str
        """

        user_input_text = input("\nType here: ")

        return user_input_text

    @staticmethod
    def press_enter_to_continue():
        """
        Method, which waits and sleep program until user don't press enter

        returns:
            None
        """

        enter_input = input('\nPress ENTER to continue.')
