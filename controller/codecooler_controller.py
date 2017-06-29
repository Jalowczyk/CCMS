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
    
