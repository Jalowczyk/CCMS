class Submission:
"""Represents submissonn object

instance atributes:
    assignment: assignment class object
    grade: None
    solution: str
    is_graded: bool
        False by defult
"""

    def __init__(self, assignment, solution):
        """Initialize submission object

        Returns
            None
        """
        self.assignment = assignment
        self.grade = None
        self.solution = solution
        self.is_graded = False
