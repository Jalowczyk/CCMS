class Attendance:
    """
    An object containing information about students attendance.
    """

    attendances = []

    def __init__(self, date, student, is_present):
        """
        Constructs an Attendance object.
        Raises ValueError is type of any argument is incorrect.

        Attributes:
            date (:obj: 'Date'): date of attendance
            student (:obj: 'Student'): Student object
            is present (bool): True for present, False for absent

        Returns:
            void
        """
        self.date = date
        self.student = student
        self.is_present = is_present

    def add_to_attendances(self):
        """
        Adds Attendance object to it's list.

        Returns:
            void
        """
        self.attendances.append(self)

    @classmethod
    def get_attendances(cls):
        return cls.attendances
