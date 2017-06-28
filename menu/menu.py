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

class ManagerMenu(EmployeeMenu):
    """
    Creates ManagerMenu obj which inherits from EmployeeMenu class.

    Class attributes:
    options: list of options
    """
    options = ["view mentors list", "add mentor", "remove mentor"] + EmployeeMenu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller depending on the user_choice.

        Parameters:
        user_choice: str
        """

        if user_choice == "view students list":
            self.codecooler_controller.view_codecoolers_action("students")
        elif user_choice == "view mentors list":
            self.codecooler_controller.view_codecoolers_action("mentors")
        elif user_choice == "add mentor":
            self.user_controller.add_codecooler_action("manager")
        elif user_choice == "remove mentor":
            self.user_controller.remove_codecooler_action("manager")
        elif user_choice == "log out":
            self.logged_user = None

class MentorMenu(EmployeeMenu):
    """
    Creates MentorMenu obj which inherits from EmployeeMenu class.

    Class attributes:
    options: list of options
    """

    options = ["add assignment", "grade submission", "check attendance",
               "add student", "edit student", "remove student"] + EmployeeMenu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller depending on the user_choice.

        Parameters:
        user_choice: str
        """

        if user_choice == "add assigment":
            self.assignment_controller.add_assignment_action()
        elif user_choice == "grade submission":
            self.submission_controller.grade_submission_action()
        elif user_choice == "check attendance":
            self.attendance_controller.check_attendance_action()
        elif user_choice == "add student":
            self.codecooler_controller.add_codecooler_action("mentor")
        elif user_choice == "remove student":
            self.user_controller.remove_codecooler_action("mentor")
        elif user_choice == "view students list":
            self.codecooler_controller.view_codecoolers_action("students")
        elif user_choice == "log out":
            self.logged_user = None

class StaffMenu(EmployeeMenu):
    """
    Creates StaffMenu obj which inherits from EmployeeMenu class.
    """

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller depending on the user_choice.

        Parameters:
        user_choice: str
        """

        if user_choice == "view students list":
            self.codecooler_controller.view_codecoolers_action("students")


class Student(Menu):
    """
    Creates StudentMenu obj which inherits from Menu class.

    Class attributes:
    options: list of Student obj
    """

    options = ["submit assignment", "show assignments"] + Menu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller depending on the user_choice.

        Parameters:
        user_choice: str
        """

        if user_choice == "submit assigment":
            self.submission_controller.submit_assignment_action()
        elif user_choice == "show assignments":
            self.assignments_controller.view_assignments_action()
        elif user_choice == "log out":
            self.logged_user = None  
