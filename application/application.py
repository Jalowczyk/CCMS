from application.menu.menu import *
from application.read_write_csv.csv_read_write import *
from application.user_input.user_input import UserInput
from application.view.view import View
import os


class Application:
    """
    Creates application obj.
    Class attributes:
    roles: dict
    options: list

    Instance attributes:
    is_running: bool
    session: dict
    menu: None/Menu obj
    user_input: UserInput obj
    view: View obj
    codecooler_data_file_path: str
    attendances_data_file_path: str
    assignments_data_file_path: str
    submissions_data_file_path: str
    """

    roles = {"Manager": ManagerMenu, "Staff": StaffMenu, "Mentor": MentorMenu,
             "Student": StudentMenu}

    options = ["log in", "exit"]

    def __init__(self):
        """
        Creates application obj.
        """
        self.is_running = True
        self.session = {"logged_user": None}
        self.menu = None
        self.view = View()
        self.user_input = UserInput(self.view)
        self.codecooler_data_file_path = "application/data/codecoolers_data.csv"
        self.attendances_data_file_path = "application/data/attendance.csv"
        self.assignments_data_file_path = "application/data/assignments.csv"
        self.submissions_data_file_path = "application/data/submissions.csv"

    def handle_login(self):
        """
        Enables to log in or exit program.
        """
        os.system("clear")
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
        os.system("clear")
        if self.session["logged_user"]:
            role = self.session["logged_user"].__class__.__name__
            self.menu = self.roles[role](self.session, self.view, self.user_input)
            self.menu.display_menu()
            user_choice = self.menu.get_user_input()
            self.menu.handle_menu(user_choice)

    def run(self):
        """
        Entry method for the main module which read csv file at the beginning
        and write to csv file at the end.
        """
        try:
            CsvHandling.read_students_from_csv(self.codecooler_data_file_path)
            CsvHandling.read_attendances_from_csv(self.attendances_data_file_path)
            CsvHandling.read_assignments_from_csv(self.assignments_data_file_path)
            CsvHandling.read_submissions_from_csv(self.submissions_data_file_path)

        except FileNotFoundError:
            CsvHandling.csv_create_if_non_exist()
            self.view.first_program_usage_message()
            self.user_input.get_anykey()

        finally:

            while self.is_running:
                self.handle_login()
                self.handle_menu()

            CsvHandling.write_codecoolers_to_csv(self.codecooler_data_file_path)
            CsvHandling.write_attendance_to_csv(self.attendances_data_file_path)
            CsvHandling.write_assignments_to_csv(self.assignments_data_file_path)
            CsvHandling.write_submissions_to_csv(self.submissions_data_file_path)

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
