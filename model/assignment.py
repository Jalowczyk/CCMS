class Assignment:

    assignments = []

    def __init__(self, title, description, max_grade):
        self.title = title
        self.description = description
        self.max_grade = max_grade
        self.submissons = []

    @classmethod
    def add_assignment(cls, assignment):
        cls.assignments.append(assignment)

    def add_submission(self, submisson):
        self.submissons.append(submisson)
