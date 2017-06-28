from controller/codecooler_controller import CodecoolerController
from controller/attendance_controller import AttendanceController
from controller/submission_controller import SubmissionController
from view/view import View

class Menu:
    """
    Creates Menu object.

    Class attributes:
    options: list

    Instance attributes:
    logged_user: Codecooler obj
    view: View obj
    user_input: UserInput obj
    codecooler_controller: CodecoolerController obj
    attendance_controller: AttendanceController obj
    submission_controller: SubmissionController obj
    assignment_controller: AssignmentController obj
    """
    options = ["log out"]


    def __init__(self, logged_user, view, user_input):
        """
        Creates Menu obj with instance attributes: logged_user, view, user_input
        Parameters:
        logged_user: Codecooler obj
        view: View obj
        user_input: UserInput obj
        """
        self.logged_user = logged_user
        self.view = view
        self.user_input = user_input
        self.codecooler_controller = CodecoolerController()
        self.attendance_controller = AttendanceController()
        self.submission_controller = SubmissionController()
        self.assignment_controller = AssignmentController()

    def display_menu(self):
        """
        Displays menu.
        """
        self.view.display_menu(self, self.options)

    def get_user_input(self):
        """
        Returns user input (str).
        """

        return self.view.get_option(self.options)

class EmployeeMenu(Menu):
    """
    Creates EmployeeMenu obj which inherits from Menu class

    Class attributes:
    options: list of options
    """
    options = ["view students list"] + Menu.options
