from application.controller.assignment_controller import AssignmentController
from application.controller.attendance_controller import AttendanceController
from application.controller.codecooler_controller import CodecoolerController
from application.controller.submission_controller import SubmissionController
import os

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

    def __init__(self, session, view, user_input):
        """
        Creates Menu obj with instance attributes: logged_user, view,
                                                   user_input
        Parameters:
        logged_user: Codecooler obj
        view: View obj
        user_input: UserInput obj
        """

        self.session = session
        self.view = view
        self.user_input = user_input
        self.codecooler_controller = CodecoolerController(user_input, view)
        self.attendance_controller = AttendanceController(user_input, view)
        self.submission_controller = SubmissionController(session, user_input, view)
        self.assignment_controller = AssignmentController(user_input, view)

    def display_menu(self):
        """
        Displays menu.
        """
        self.view.show_greeting(self.session)
        self.view.show_menu_option(self.options)

    def get_user_input(self):
        """
        Returns user input (str).
        """

        return self.user_input.get_option(self.options)


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

    options = ["view mentors list", "edit mentor", "add mentor", "remove mentor"] + EmployeeMenu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller
        depending on the user_choice.

        Parameters:
        user_choice: str
        """
        os.system("clear")
        if user_choice == "view students list":
            self.codecooler_controller.show_codecooler_action("student")
        elif user_choice == "view mentors list":
            self.codecooler_controller.show_codecooler_action("mentor")
        elif user_choice == "add mentor":
            self.codecooler_controller.add_codecooler_action("mentor")
        elif user_choice == "remove mentor":
            self.codecooler_controller.remove_codecooler_action("mentor")
        elif user_choice == "edit mentor":
            self.codecooler_controller.edit_codecooler_action("mentor")
        elif user_choice == "log out":
            self.session["logged_user"] = None


class MentorMenu(EmployeeMenu):
    """
    Creates MentorMenu obj which inherits from EmployeeMenu class.

    Class attributes:
    options: list of options
    """

    options = ["add assignment", "show assignments", "grade submission", "check attendance",
               "view attendance", "add student", "edit student", "remove student"] + EmployeeMenu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller
        depending on the user_choice.

        Parameters:
        user_choice: str
        """
        os.system("clear")
        if user_choice == "add assignment":
            self.assignment_controller.add_assignment_action()
        elif user_choice == "show assignments":
            self.assignment_controller.show_assignments_details()
        elif user_choice == "grade submission":
            self.submission_controller.set_grade_action()
        elif user_choice == "check attendance":
            self.attendance_controller.check_attendance_action()
        elif user_choice == "add student":
            self.codecooler_controller.add_codecooler_action("student")
        elif user_choice == "edit student":
            self.codecooler_controller.edit_codecooler_action("student")
        elif user_choice == "remove student":
            self.codecooler_controller.remove_codecooler_action("student")
        elif user_choice == "view students list":
            self.codecooler_controller.show_codecooler_action("student")
        elif user_choice == "view attendance":
            self.attendance_controller.view_attendance_action()
        elif user_choice == "log out":
            self.session["logged_user"] = None

        enter = input("ENTER!!!") #for testing purposes only (because Szymon hasn't
                                  #done it yet)


class StaffMenu(EmployeeMenu):
    """
    Creates StaffMenu obj which inherits from EmployeeMenu class.
    """

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller
        depending on the user_choice.

        Parameters:
        user_choice: str
        """
        os.system("clear")
        if user_choice == "view students list":
            self.codecooler_controller.show_codecooler_action("student")
        elif user_choice == "log out":
            self.session["logged_user"] = None


class StudentMenu(Menu):
    """
    Creates StudentMenu obj which inherits from Menu class.

    Class attributes:
    options: list of Student obj
    """

    options = ["submit assignment", "show assignments", "show grades"] + Menu.options

    def handle_menu(self, user_choice):
        """
        Redirects to proper action in proper controller
        depending on the user_choice.

        Parameters:
        user_choice: str
        """
        os.system("clear")
        if user_choice == "submit assignment":
            self.submission_controller.add_submission_action()
        elif user_choice == "show assignments":
            self.assignment_controller.show_assignments_details()
        elif user_choice == "show grades":
            self.submission_controller.check_grade_action()
        elif user_choice == "log out":
            self.session["logged_user"] = None
