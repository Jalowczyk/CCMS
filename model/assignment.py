class Assignment:
    """Represents assignment object

    class atribute:
        assignment: list
            list of assignments objects

    instance atributes:
        title: str
        description: str
        max_grade: int
        submissons: list
            list of submissions objects, connected to assignmnet
    """

    assignments = []

    def __init__(self, title, description, max_grade):
        """Initialize assignment object

        returns: None
        """
        self.title = title
        self.description = description
        self.max_grade = max_grade
        self.submissons = []

    @classmethod
    def add_assignment(cls, assignment):
        """Adds assignment object to class list

        Parameter:
            assignment: object of assignment class

        Returns:
            None
        """
        cls.assignments.append(assignment)

    def add_submission(self, submisson):
        """Add submisson connected to assignment object

        Parameters:
            submisson: object of submisson class

        Returns:
            None
        """
        self.submissons.append(submisson)

    def get_title(self):
        """Gets title atribute of instance

        Returns
            title: str
        """
        return self.title

    def get_description(self):
        """Gets title atribute of instance

        Returns
            title: str
        """
        return self.description

    def get_max_grade(self):
        """Gets max_grade atribute of instance

        Returns
            max_grade: int
        """
        return self.max_grade
