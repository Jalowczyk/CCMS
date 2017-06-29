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
        message = 'Please provide link to submit:'
        self.view.show_message(message)
        solution = self.user_input.get_text_input()
        submisson = Submisson(self.logged_student, assignment, solution)
        assignment.add_submission(submisson)
        self.logged_user.add_submission(submisson)

    def set_grade_action(self):
        """Sets grade atribute of submission and set as graded

        Returns: None
        """
        options = ["Grade by student", "Grade by assignment"]
        self.view.show_menu_option(options)
        option = self.user_input.get_menu_input(options)
        if option == option[0]:
            submissons = self.grade_by_student_action()
        elif option == option[1]:
            submissons = self.grde_by_assignment_action()

        self.view.show_submissions(submissons)
        submission_index = self.user_input.get_index_input(len(submissons))
        submission = submissons[submission_index]
        message = "How much poits you want to assign?"
        self.view.show_message(message)
        grade = user_input.get_numeric_input
        submission.set_grade(grade)
        submission.set_is_graded()

    def check_grade_action(self):
        """Shows grades of user_input

        Return: None
        """
        submissions = self.logged_user.get_submission()
        self.view.show_grades(submissions)

    def get_submissions_from_student(self):
        """Gets submission instance list of Student object

        Returns:
            submissions: list of submissions object
        """
        students = Student.get_students()
        self.view.show_codecoolers(students)
        student_index = self.user_input.get_index_input(len(students))
        student = students[student_index]
        submissons = student.get_submissions()
        return submissons

    def get_submissions_from_assignment(self):
        """Gets submission instance list of Assignment object

        Returns:
            submissions: list of submissions object
        """
        assignment = Assignment.get_assignments()
        self.view.show_assignments(assignment)
        assignment_index = self.user_input.get_index_input(len(assignments))
        assignment = assignments[assignment_index]
        submissons = assignment.get_submissions()
        return submissons
