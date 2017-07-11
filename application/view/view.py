import prettytable

class View:
    """
    Creates View obj.
    """
    def __init__(self):
        self.table = PrettyTable()

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
        self.table.clear_rows()
        self.table.field_names = ["Index", "First name", "Last name"]

        for index, codecooler in enumerate(codecoolers):
            self.table.add_row([index + 1, codecooler.get_first_name(),
                                    codecooler.get_last_name()])
        print(self.table)

    def show_codecooler(self, codecooler):
        """
        Prints specific codecooler data.
        Parameters:
        codecooler: Codecooler obj
        """
        self.table.clear_rows()
        self.table.field_names = ["First name", "Last name", "E-mail"]
        self.table.add_row([codecooler.get_first_name(),
                                 codecooler.get_last_name(), codecooler.get_email()])
        print(self.table)

    def show_assignments(self, assignments):
        """
        Prints assignments information.
        Parameters:
        assignments: list
        """
        self.table.clear_rows()
        self.table.field_names = ["Index", "Assignment's title"]

        for index, assignment in enumerate(assignments):
            self.table.add_row([index + 1, assignment.get_title()])

        print(self.table)

    def show_submissions(self, submissions):
        """
        Prints assignments information.
        Parameters:
        assignments: list
        """
        self.table.clear_rows()
        self.table.field_names = ["Index", "Student's first name", "Student's last name",
                                  "Assignment's title"]

        for index, submission in enumerate(submissions):
            self.table.add_row([index + 1, submission.get_student().get_first_name(),
                                        submission.get_student().get_last_name(),
                                        submission.get_assignment().get_title()])

        print(self.table)

    def show_assignment_details(self, assignment):
        """
        Prints specific assignment information.
        Parameters:
        assignment: Assignment obj
        """
        self.table.clear_rows()
        self.table.field_names = ["Title", "Maximum grade", "Description"]

        self.table.add_row([assignment.get_title(), assignment.get_max_grade(),
                                    assignment.get_description()])

        print(self.table)


    def show_message(self, message):
        """
        Prints message.
        Parameters:
        message: str
        """

        RED = '\033[91m'
        WHITE = '\033[0m'

        print(RED + "\n" + message + "\n" + WHITE)

    def show_grades(self, submissions):
        """
        Prints student submissions grades.
        Parameters:
        submissions: list
        """
        self.table.clear_rows()
        self.table.field_names = ["Index", "Assignment's title",
                                  "Student's grade", "Maximum grade"]

        for index, submission in enumerate(submissions):
            assignment = submission.get_assignment().get_title()
            if submission.get_grade():
                self.table.add_row([index + 1, assignment, submission.get_grade(),
                                             submission.get_assignment().get_max_grade()])
            else:
                self.table.add_row([index + 1, assignment, "not graded",
                                    submission.get_assignment().get_max_grade()])
        print(self.table)
