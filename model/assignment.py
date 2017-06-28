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
