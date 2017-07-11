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
            is_present (bool): True for present, False for absent

        Returns:
            void
        """
        if date is None:
            raise ValueError('date should be Datetime object')
        if student is None:
            raise ValueError("student should be Student Class object")
        if is_present is None:
            raise ValueError("is_present should be boolw")
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
        """
        Returns attendances list (class attribute).

        Returns:
        attendances (list of :obj: 'Attendance'): list of attendances objects
        """

        return cls.attendances

    def get_date(self):
        return self.date

    def get_student(self):
        return self.student

    def get_is_present(self):
        return self.is_present
