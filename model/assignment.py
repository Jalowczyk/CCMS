class Assignment:
    """Represents assignment object

    class attribute:
        assignment: list
            list of assignments objects

    instance attributes:
        title: str
        description: str
        max_grade: int
        submissions: list
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
        self.submissions = []

    def add_to_assignments(self):
        """Adds assignment object to class list

        Parameter:
            self: object of assignment class

        Returns:
            None
        """
        self.assignments.append(self)

    def add_submission(self, submission):
        """Add submission connected to assignment object

        Parameters:
            submission: object of submission class

        Returns:
            None
        """
        self.submissions.append(submission)

    def get_title(self):
        """Gets title attribute of instance

        Returns
            title: str
        """
        return self.title

    def get_description(self):
        """Gets description attribute of instance

        Returns
            description: str
        """
        return self.description

    def get_max_grade(self):
        """Gets max_grade attribute of instance

        Returns
            max_grade: int
        """
        return self.max_grade

    def get_submissions(self):
        """Gets submissions attribute of instance

        Returns
            submission: list of submission class objects
        """
        return self.submissions

    @classmethod
    def get_assignments_list(cls):
        """Gets assignments attribute of class

        Returns
            assignments = list of assignments class objects
        """
        return cls.assignments
