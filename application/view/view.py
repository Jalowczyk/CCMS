import os


class View:
    """
    Creates View obj.
    """
    def show_greeting(self, session):
        codecooler = session["logged_user"]

        print(Colors.BLUE + "Hello {}!".format(codecooler.__class__.__name__))
        print("You are logged as {} {}.\n".format(codecooler.get_first_name(),
              codecooler.get_last_name()))
        print(Colors.WHITE, end="")

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

        print("\n{} {}: {}".format(codecooler.get_first_name(),
              codecooler.get_last_name(), codecooler.get_email()))

    def show_attendance_details(self, student):
        print("\n{} {}:".format(student.get_first_name().upper(), student.get_last_name().upper()))
        for index, attendance in enumerate(student.get_attendance()):
            if attendance.get_is_present:
                print("{}. {}: {}".format(index + 1, attendance.get_date(), "present"))
            else:
                print("{}. {}: {}".format(index + 1, attendance.get_date(), "absent"))

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

        print("\n{}: {}".format("Title", assignment.get_title()))
        print("{}: {}".format("Maximum grade", assignment.get_max_grade()))
        print("{}: {}".format("Description", assignment.get_description()))

    def show_attendance(self, index, student, percent_attendance):

        print("{}. {} {}: {}%".format(index, student.get_first_name(),
              student.get_last_name(), percent_attendance))

    def show_message(self, message):
        """
        Prints message.
        Parameters:
        message: str
        """

        print(Colors.RED + "\n" + message + "\n" + Colors.WHITE)

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

    def first_program_usage_message(self):
        """
        Prints message after first run of the program.
        """
        print(Colors.RED + 'This is the first run of the program. Default values of manager account are:\n\
               First name: Admin\n\
               Last_name: Adminsky\n\
               email: admin.adminsky@cc.pl\n\
               password: dupa\n\
               You can change this date later.' + Colors.WHITE)

    def clear(self):
        os.system("clear")


class Colors:

    BLUE = '\033[94m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    END = '\033[0m'
    RED = '\033[91m'
    WHITE = '\033[0m'
