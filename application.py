import sys


class Application:

    roles = {"manager": ManagerMenu, "staff": StaffMenu, "mentor": MentorMenu,
             "student": StudentMenu}

    options = ["log in", "exit"]

    def __init__(self):
        self.user_input = user_input
        self.view = view
        self.logged_user = {"logged_user": None}

    

    def log_in(self):
        email, password = self.user_input.get_login_input()
        codecoolers = Manager.get_managers() + Staff.get_staff() + Mentor.get_mentors() + Student.get_students()

        for codecooler in codecoolers:
            if email == codecooler.get_email() and password == codecooler.get_password():
                return codecooler
            else:
                self.view.view_error("\nWrong login or password!\n")
                return None
