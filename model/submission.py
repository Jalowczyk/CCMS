class Submission:
    """Represents submissonn object

    instance atributes:
        student: student class object
        assignment: assignment class object
        grade: None
        solution: str
        is_graded: bool
            False by defult
    """

    def __init__(self, student, assignment, solution):
        """Initialize submission object

        Returns
            None
        """
        self.student = student
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

    def set_grade(self, grade):
        """Sets grade attribute of instance


        Returns
            void:
        """
        self.grade = grade

    def set_is_graded(self, is_graded):
        """Sets is_graded attribute of instance

        Returns
            void:
        """
        self.is_graded = is_graded

        Returns
            void:
        """
        self.grade = grade

  

    def get_assignment(self):
        """Gets assignment attribute of instance

        Returns
            assignment: object of assignment class
        """
        return self.assignment

    def get_is_graded(self):
        """Gets is_grade attribute of instance

        Returns
            is_graded: bool
        """
        return self.is_graded

    def get_solution(self):
        """Gets solution attribute of instance

        Returns
            solution: str
        """
        return self.solution

    def get_student(self):
        """Gets student attribute of instance

        Returns
            student: Student obj
        """
        return self.student
