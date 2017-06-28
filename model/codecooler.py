class Codecooler:
    """
    Parent class for Employee and Student class.

    Attributes:
    first_name(str) - instance attrubute storing employee's or student's first name
    last_name(str) - instance attrubute storing employee's or student's last name
    email(str) - instance attrubute storing employee's or student's email
    password(str) - instance attrubute storing employee's or student's password
    """

    def __init__(self, first_name, last_name, email, password):
        """
        Create Codecooler object with instance attributes: first_name, last_name,
        email, password.

        Parameters:
        first_name: str
        last_name: str
        email: str
        password: str
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_first_name(self):
        """
        Returns first_name instance attribute.

        Returns:
        first_name: str
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns last_name instance attribute.

        Returns:
        last_name: str
        """
        return self.last_name

    def get_email(self):
        """
        Returns email instance attribute.

        Returns:
        email: str
        """
        return self.email

    def get_password(self):
        """
        Returns password instance attribute.

        Returns:
        password: str
        """
        return self.password

    def set_first_name(self, first_name):
        """
        Set first_name instance attribute to first_name parameter.

        Parameters:
        first_name: str
        """
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        Set last_name instance attribute to last_name parameter.

        Parameters:
        last_name: str
        """
        self.last_name = last_name

    def set_password(self, password):
        """
        Set password instance attribute to password parameter.

        Parameters:
        password: str
        """
        self.password = password

    def set_email(email):
        """
        Set email instance attribute to email parameter.

        Parameters:
        email: str
        """
        self.email = email

class Employee(Codecooler):
    """
    Codecooler's child class which creates Employee's object.
    """

class Manager(Employee):
    """
    Employee's child class.
    Class attributes:
    managers (list): class attribute storing Manager's objects
    """

    managers = []

    def add_to_managers(self):
        """
        Adds Manager object to managers list (class attribute).
        """
        self.managers.append(self)

class Mentor(Employee):
    """
    Creates Mentor object.

    Class attributes:
    mentors (list): list storing Mentor objects
    """

    mentors = []

    @classmethod
    def get_mentors(cls):
        """
        Returns mentors list (class attribute).

        Returns:
        mentors: list
        """
        return cls.mentors

    def add_to_mentors(self):
        """
        Adds Mentor object to mentors list (class attribute).
        """
        self.mentors.append(self)

    def remove(self):
        """
        Removes Mentor object from mentors list (class attribute).
        """
        self.mentors.remove(self)

class Stuff(Employee):
    """
    Creates Stuff object.

    Class attributes:
    stuff(list): list storing Stuff objects
    """

    stuff = []

    def add_to_stuff(self):
        """
        Adds Stuff object to stuff list (class attribute).
        """
        self.stuff.append(self)

class Student(Codecooler):
    """
    Creates Student object.

    Class attributes:
    students(list): list storing Student objects
    Instance attributes:
    submissions(list): list storing Submission objects
    attendance(list): list storing Attendance objects
    """

    students = []

    def __init__(self):
        """
        Creates Student obj.
        """
        self.submissions = []
        self.attendance = []

    @classmethod
    def get_students(cls):
        """
        Returns students list (class attribute).

        Returns:
        students: list
        """
        return cls.students

    def add(self):
        """
        Adds Student object to students list (class attribute).
        """
        self.students.append(self)

    def remove(self):
        """
        Removes Student object from students list (class attribute).
        """
        self.students.remove(self)

    def get_attendance(self):
        """
        Returns attendance list (instance attribute).

        Returns:
        attendance: list
        """
        return self.attendance

    def get_submissions(self):
        """
        Returns submissions list (instance attribute).

        Returns:
        submissions: list
        """
        return self.submissions

    def add_submission(self, submission):
        """
        Adds Submission object to submissions list (instance attribute).

        Parameters:
        submission: Submission obj
        """
        self.submissions.append(submission)

    def add_attendance(self, attendance):
        """
        Adds Attendance object to attendance list (instance attribute).

        Parameters:
        attendance: Attendance obj
        """
        self.attendance.append(attendance)
