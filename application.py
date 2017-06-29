import sys


class Application:

    roles = {"Manager": ManagerMenu, "Staff": StaffMenu, "Mentor": MentorMenu,
             "Student": StudentMenu}

    options = ["log in", "exit"]

    def __init__(self):
        self.is_running = True
        self.user_input = UserInput()
        self.view = View()
        self.session = {"logged_user": None}
        self.menu = None


    def handle_login(self):

        while not self.session["logged_user"]:
            user_option = self.input.get_option(self.options)
            if user_option == "log in":
                self.logged_user["logged_user"] = self.log_in()
            elif user_option == "exit":
                self.is_running = False
                break

    def handle_menu(self):

        if self.session["logged_user"]:
            role = self.session["logged_user"].__class__.__name__
            self.menu = self.roles[role](self.session["logged_user"], self.view, self.user_input)
            self.menu.display_menu()
            user_choice = self.menu.get_user_input()
            self.menu.handle_menu(user_choice)


    def log_in(self):
        email, password = self.user_input.get_login_input()
        codecoolers = Manager.get_managers() + Staff.get_staff() + Mentor.get_mentors() + Student.get_students()

        for codecooler in codecoolers:
            if email == codecooler.get_email() and password == codecooler.get_password():
                return codecooler
            else:
                self.view.view_error("\nWrong login or password!\n")
                return None
