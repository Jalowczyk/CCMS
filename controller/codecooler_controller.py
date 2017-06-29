from model.codecooler import Mentor
from model.codecooler import Student


class CodecoolerController:

    def __init__(self, view, user_input):
        self.view = view
        self.user_input = user_input

    def show_codecooler_action(self, user_role):
        options = ["show details", "back"]

        if user_role == "mentor":
            self.view.show_codecooler(Mentor.get_mentors())
            self.view.show_menu_option(options)
            option = self.input.get_menu_input(options)
            if main option == options[0]:
                returns ""  # To finish
        elif user_role == "student":
            self.view.show_codecooler(Student.get_students())


    def add_codecooler_action(self, person_role):
        if person_role == "mentor":
            mentor = Mentor(self.user_input.get_codecooler_data())
            mentor.add()
        elif person_role == "student":
            student = Student(self.user_input.get_codecooler_data())
            student.add()

    def edit_codecooler_action(self, person_role):
        if person_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecoolers(mentors)
            option = self.user_input.get_record_by_index(len(mentors))
            mentor = mentors[option]
            data = self.user_input.get_codecooler_data()
            mentor.set_name = data["name"]
            mentor.set_surname = data["surname"]
            mentor.set_email = data["email"]
            mentor.set_password = data["password"]
        elif person_role == "student":
            students = Student.get_students()
            self.view.show_codecoolers(students)
            option = self.user_input.get_record_by_index(len(students))
            student = students[option]
            data = self.user_input.get_codecooler_data()
            student.set_name = data["name"]
            student.set_surname = data["surname"]
            student.set_email = data["email"]
            student.set_password = data["password"]

    def remove_codecooler_action(self, person_role):
        if person_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecoolers(mentors)
            option = self.input.get_record_by_index(len(mentors))
            mentor = mentors[option]
            Mentor.remove(mentor)

        elif person_role == "student":
            students = Student.get_students()
            self.view.show_codecoolers(students)
            option = self.input.get_record_by_index(len(students))
            student = students[option]
            Student.remove(student)
