class SumbmissionController:
    """Represents SumbmissionController object

    Atributes:
        user_input: object of UserInput class
        view: object of View class
        logged_user: object of Codecooler class
    """

    def __init__(self, user_input, view, logged_user):
        """Instance initizialer
        """
        self.user_input = user_input
        self.view = view
        self.logged_user = logged_user

    def add_submission_action(self, assignment):
        """Adds submission to class list in Submission

        Returns: None
        """
        solution = self.user_input.get_submission_solution()data
        submisson = Submisson(self.logged_student, assignment, solution)
        assignment.add_submission(submisson)
        self.logged_user.add_submission(submisson)

    def get_assignment(self):
        """Gets object of assignment class

        Return: Assignment object
        """
        assignments = Assignment.get_assignments_list()
        index = self.user_input.get_index_input(len(assignments))
        assignment = assignments[index]
        return assignment

    def get_submission(self):
        """Gets submission object from instance list of assignment

        Returns: submission object
        """
        assignment = self.get_assignment()
        submissions_list = assignment.get_submissions()
        index = self.user_input.get_index_input(len(submissions_list))
        submission = submissions_list[index]
        return submission

    def set_grade_action(self):
        """Sets grade atribute of submission and set as graded7

        Returns: None
        """
        submission = get_submission
        grade = self.user_input.get_grade()
        submission.set_grade(grade)
        submission.set_is_graded()

    def check_grade_action(self):
        """Shows grades of user_input

        Return: None
        """
        submissions = self.logged_user.get_submission()
        self.view.show_grades(submissions)
