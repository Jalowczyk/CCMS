class View:
    """
    Creates View obj.
    """
    def __init__(self):
        self.table = TextTable()

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
            print("{}.{} {}".format(index + 1, codecooler.get_first_name(),
                                    codecooler.get_last_name()))

    def show_codecooler(self, codecooler):
        """
        Prints specific codecooler data.
        Parameters:
        codecooler: Codecooler obj
        """

        print("{} {}: {}".format(codecooler.get_first_name(),
                                 codecooler.get_last_name(), codecooler.get_email()))

    def show_assignments(self, assignments):
        """
        Prints assignments information.
        Parameters:
        assignments: list
        """

        for index, assignment in enumerate(assignments):
            print("{}. {}".format(index + 1, assignment.get_title()))

    def show_submissions(self, submissions):
        """
        Prints assignments information.
        Parameters:
        assignments: list
        """

        for index, submission in enumerate(submissions):
            print("{}. {} {} {}".format(index + 1, submission.get_student().get_first_name(),
                                        submission.get_student().get_last_name(),
                                        submission.get_assignment().get_title()))

    def show_assignment_details(self, assignment):
        """
        Prints specific assignment information.
        Parameters:
        assignment: Assignment obj
        """

        print("{}: {}".format("Title", assignment.get_title()))
        print("{}: {}".format("Maximum grade", assignment.get_max_grade()))
        print("{}: {}".format("Description", assignment.get_description()))

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

        for index, submission in enumerate(submissions):
            assignment = submission.get_assignment().get_title()
            if submission.get_grade():
                print("{}. {}: {}/{}".format(index + 1, assignment, submission.get_grade(),
                                             submission.get_assignment().get_max_grade()))
            else:
                print("{}. {}: {}".format(index + 1, assignment, "not graded"))
