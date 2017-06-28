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

    def get_grade(self):
        """Gets grade atribute of instance

        Returns
            grade: int
        """
        return self.grade

    def get_assignment(self):
        """Gets assignment atibute of instance

        Returns
            assignment: object of assignment class
        """
        return self.assignment

    def get_is_graded(self):
        """Gets is_grade atibute of instance

        Returns
            is_graded: bool
        """
        return self.is_graded
