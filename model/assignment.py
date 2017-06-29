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
    def get_assignments(cls):
        """
        Returns assignment list (class attribute).

        Returns:
        assignment (list of :obj: 'Assignment'): list of assignment objects
        """
        return cls.assignments

    def add_to_assignments(self):
        """Adds assignment object to class list

        Parameter:
            self: object of assignment class

        Returns:
            None
        """
        self.assignments.append(self)

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
        """Gets description atribute of instance

        Returns
            description: str
        """
        return self.description

    def get_max_grade(self):
        """Gets max_grade atribute of instance

        Returns
            max_grade: int
        """
        return self.max_grade

    def get_submission(self):
        """Gets submissons atribute of instance

        Returns
            submisson: list of submisson class objects
        """
        return self.submissons
