from model.assignment import Assignment
from model.codecooler import Student
from model.submission import Submission


class SubmissionController:
    """Represents SubmissionController object

    Attributes:
        user_input: object of UserInput class
        view: object of View class
        logged_user: object of Codecooler class
    """

    def __init__(self, session, user_input, view):
        """Instance initializer
        """
        self.session = session
        self.user_input = user_input
        self.view = view

    def add_submission_action(self):
        """Adds submission to class list in Submission

        Returns: None
        """
        assignments = Assignment.get_assignments_list()
        self.view.show_assignments(assignments)
        message = 'Choose assignment: '
        self.view.show_message(message)
        index = self.user_input.get_index_input(len(assignments))
        assignment = assignments[index]
        message = 'Please provide link to submit:'
        self.view.show_message(message)
        solution = self.user_input.get_text_input()
        submission = Submission(self.session["logged_user"], assignment, solution)
        assignment.add_submission(submission)
        self.session["logged_user"].add_submission(submission)

    def set_grade_action(self):
        """Sets grade attribute of submission and set as graded

        Returns: None
        """
        options = ["Grade by student", "Grade by assignment"]
        self.view.show_menu_option(options)
        option = self.user_input.get_option(options)
        if option == options[0]:
            submissions = self.get_submissions_from_student()
        elif option == options[1]:
            submissions = self.get_submissions_from_assignment()

        self.view.show_submissions(submissions)
        submission_index = self.user_input.get_index_input(len(submissions))
        submission = submissions[submission_index]
        message = "How much points you want to assign?"
        self.view.show_message(message)
        grade = self.user_input.get_numeric_input
        submission.set_grade(grade)
        submission.set_is_graded()

    def check_grade_action(self):
        """Shows grades of user_input

        Return: None
        """
        submissions = self.session["logged_user"].get_submissions()
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
        submissions = student.get_submissions()
        return submissions

    def get_submissions_from_assignment(self):
        """Gets submission instance list of Assignment object

        Returns:
            submissions: list of submissions object
        """
        assignments = Assignment.get_assignments_list()
        self.view.show_assignments(assignments)
        assignment_index = self.user_input.get_index_input(len(assignments))
        assignment = assignments[assignment_index]
        submissions = assignment.get_submissions()
        return submissions
