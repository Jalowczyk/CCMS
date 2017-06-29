from model.codecooler import Mentor
from model.codecooler import Student


class CodecoolerController:
    """Represeent CodecoolerController objects

    instance Attributes:
        viev: object of viev class
        input: objet of input class
    """

    def __init__(self, user_input, viev):
        self.user_input = user_input
        self.view = view

    def show_codecooler_details_action(self, users_list):
        """Show details of choosen user_input

        Parameters:
            user_list: list of codecoolers class objects
        Returns:
            None
        """
        message = 'Please choose index of user:'
        self.view.show_message(message)
        user_index = self.user_input.get_record_by_index(len(users_list))
        user = users_list[user_index]
        self.view.show_user_details(user)

    def show_codecooler_action(self, user_role):
        """Show codecoolers and their details

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        options = ["show details", "back"]

        if user_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecooler(mentors)
            self.view.show_menu_option(options)
            option = self.input.get_menu_input(options)
            if option == options[0]:
                self.show_codecooler_details_action(mentors)
        elif user_role == "student":
            students = Studet.get_students()
            self.view.show_codecooler(students)
            self.view.show_menu_option(options)
            option = self.input.get_menu_input(options)
            if option == options[0]:
                self.show_codecooler_details_action(students)

    def add_codecooler_action(self, person_role):
        """Create and add codecooler object to class list

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        message = 'Plese provide user data:'
        self.view.show_message(message)
        if person_role == "mentor":
            mentor = Mentor(self.user_input.get_codecooler_data())
            mentor.add()
        elif person_role == "student":
            student = Student(self.user_input.get_codecooler_data())
            student.add()

    def edit_codecooler_action(self, person_role):
        """Edits codecooler object atributes

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        message = 'Plese provide user data:'
        self.self.view.show_message(message)
        if person_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecoolers(mentors)
            option = self.user_input.get_record_by_index(len(mentors))
            mentor = mentors[option]
            data = self.user_input.get_codecooler_data()
            mentor.set_name = data["name"]
            mentor.set_surname = data["surname"]
            mentor.set_email = data["email"]
            mentor.set_password = data['password']

        elif person_role == "student":
            students = Student.get_students()
            self.view.show_codecoolers(students)
            option = self.user_input.get_record_by_index(len(students))
            student = students[option]
            data = self.user_input.get_codecooler_data()
            student.set_name = data["name"]
            student.set_surname = data["surname"]
            student.set_email = data["email"]
            student.set_password = data['password']

    def remove_codecooler_action(self, person_role):
        """Remove codecooler object from class list

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        message = 'Plese choose user to remove:'
        self.view.show_message(message)
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
