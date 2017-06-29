import sys


class Application:

    roles = {"manager": ManagerMenu, "staff": StaffMenu, "mentor": MentorMenu,
             "student": StudentMenu}

    options = ["log in", "exit"]

    def __init__(self):
        self.user_input = user_input
        self.view = view
        self.logged_user = {"logged_user": None}

    
