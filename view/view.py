from model.attendance import Attendance
from model.codecooler import Codecooler
from model.submission import Submission
from model.assignment import Assignment


class View:
    """
    Creates View obj.
    """

    def show_menu_option(self, options):
        """
        Prints menu options.
        Parameters:
        options: list
        """
        for index, option in enumerate(options):
            print("{}. {}".format(index + 1, option))

    def show_codecoolers(self, codecoolers):
        """
        Prints every codecooler data from codecoolers list.
        Parameters:
        codecoolers: list
        """

        for index, codecooler in enumerate(codecoolers):
            print("{}.{} {}: {}".format(index + 1, codecooler.get_first_name(),
                                    codecooler.get_last_name(), get_email()))

    def show_codecooler(self, codecooler):
        """
        Prints specific codecooler data.
        Parameters:
        codecooler: Codecooler obj
        """

        print("{} {}: {}".format(codecooler.get_first_name(),
                                 codecooler.get_last_name(), get_email()))

    def show_assignments(self, assignments):
        """
        Prints assignments information.
        Parameters:
        assignments: list
        """

        for index, assignment in enumerate(assignments):
            print("{}. {}".format(index + 1, assignment.get_title()))

    def show_assignment_details(self, assignment):
        """
        Prints specific assignment information.
        Parameters:
        assignment: Assignment obj
        """

        print("{}: {}".format("Title", assignment.get_title()))
        print("{}: {}".format("Maximum grade", assignment.get_max_grade()))
        print("{}: {}".format("Desctiption", assignment.get_description()))

    def show_message(self, message):
        """
        Prints message.
        Parameters:
        message: str
        """

        RED = '\033[91m'
        WHITE = '\033[0m'

        print(RED + message + WHITE)

    
