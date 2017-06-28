class Codecooler:
    "Parent class for Employee and Student class"

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

class Manager(Employee):

    managers = []

    def add_to_managers(self):
        self.managers.append(self)

class Mentor(Employee):

    mentors = []

    @classmethod
    def get_mentors(cls):
        return cls.mentors

    def add_to_mentors(self):
        self.mentors.append(self)

    def remove(self):
        self.mentors.remove(self)

class Stuff(Employee):

    stuff = []

    def add_to_stuff(self):
        self.stuff.append(self)

class Student(Codecooler):

    students = []

    def __init__(self):
        self.submissions = []
        self.attendance = []

    @classmethod
    def get_students(cls):
        return cls.students

    def add(self):
        self.students.append(self)

    def remove(self):
        self.students.remove(self)

    def get_attendance(self):
        return self.attendance

    def get_submissions(self):
        return self.submissions

    def add_submission(self, submission):
        self.submissions.append(submission)

    def add_attendance(self, attendance):
        self.attendance.append(attendance)
