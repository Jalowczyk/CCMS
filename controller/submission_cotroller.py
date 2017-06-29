class SumbmissionController:

    def __init__(self, user_input, view, logged_user):
        self.user_input = user_input
        self.view = view
        self.logged_student = logged_user

    def add_submission_action(self, assignment):
        solution = self.user_input.get_submission_solution()data
        submisson = Submisson(self.logged_student, assignment, solution)
        assignment.add_submission(submisson)

    def get_assignment(self):
        assignments = Assignment.get_assignments_list()
        index = self.user_input.get_index_input(len(assignments))
        assignment = assignments[index]
        return assignment

    def get_submission(self):
        assignment = self.get_assignment()
        submissions_list = assignment.get_submissions()
        index = self.user_input.get_index_input(len(submissions_list))
        submission = submissions_list[index]
        return submission

    def set_grade_action(self):
        submission = get_submission
        grade = self.user_input.get_grade()
        submission.set_grade(grade)
        submission.set_is_graded
