class Codecooler:

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_first_name():
        return self.first_name

    def get_last_name():
        return self.last_name

    def get_email():
        return self.email

    def get_password():
        return self.password

    def set_first_name(first_name):
        self.first_name = first_name

    def set_last_name(last_name):
        self.last_name = last_name

    def set_password(password):
        self.password = password

    def set_email(email):
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
