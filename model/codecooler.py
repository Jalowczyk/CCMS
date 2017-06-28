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

    
    # + get_students(): list
    # + add(): void
    # + remove(): void
    # + get_attendance(): void
    # + get_submissions(): list
    # + add_submission(submission): void
    # + add_attendance(attendance): void
