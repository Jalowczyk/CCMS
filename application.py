from model.codecooler import *
from user_input.user_input import UserInput
from menu.menu import *
from view.view import View
from csv_read_write import *


class Application:
    """
    Creates Application obj.
    Class attributes:
    roles: dict
    options: list

    Instance attributes:
    is_running: bool
    session: dict
    menu: None/Menu obj
    user_input: UserInput obj
    view: View obj
    path: str
    """

    roles = {"Manager": ManagerMenu, "Staff": StaffMenu, "Mentor": MentorMenu,
             "Student": StudentMenu}

    options = ["log in", "exit"]

    def __init__(self):
        """
        Creates Application obj.
        """
        self.is_running = True
        self.session = {"logged_user": None}
        self.menu = None
        self.user_input = UserInput()
        self.view = View()
        # self.filename = "data/"
        # self.data_manager = DataManager(self.path)


    def handle_login(self):
        """
        Enables to log in or exit program.
        """

        while not self.session["logged_user"]:
            self.view.show_menu_option(self.options)
            user_option = self.user_input.get_option(self.options)
            if user_option == "log in":
                self.session["logged_user"] = self.log_in()
            elif user_option == "exit":
                self.is_running = False
                return

    def handle_menu(self):
        """
        Directs the user to the proper menu, depending on the user role.
        """

        if self.session["logged_user"]:
            role = self.session["logged_user"].__class__.__name__
            self.menu = self.roles[role](self.session["logged_user"], self.view, self.user_input)
            self.menu.display_menu()
            user_choice = self.menu.get_user_input()
            self.menu.handle_menu(user_choice)

    def run(self):
        """
        Entry method for the main module which read csv file at the beginning
        and write to csv file at the end.
        """
        read_students_from_csv("codecoolers_data.csv")
        read_attendances_from_csv("attendance.csv")
        read_assignments_from_csv("assignments.csv")
        read_submissions_from_csv("submissions.csv")

        while self.is_running:
            self.handle_login()
            self.handle_menu()

        write_codecoolers_to_csv("codecoolers_data.csv")
        write_attendance_to_csv("attendance.csv")
        write_assignments_to_csv("assignments.csv")
        write_submissions_to_csv("submissions.csv")

    def log_in(self):
        """
        Compares user email and password input to objects email and
        password attributes, and if they are ok, returns user object, otherwise
        returns None.

        Returns:
        codecooler: obj
        None
        """
        email, password = self.user_input.get_login_input()
        codecoolers = Manager.get_managers() + Staff.get_staff() + Mentor.get_mentors() + Student.get_students()
        for codecooler in codecoolers:
            if email == codecooler.get_email() and password == codecooler.get_password():
                return codecooler
        self.view.show_message("\nWrong login or password!\n")
        return None
