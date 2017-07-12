from application.model.codecooler import Mentor
from application.model.codecooler import Student


class CodecoolerController:
    """Represeent CodecoolerController objects

    instance Attributes:
        view: object of view class
        input: object of input class
    """

    def __init__(self, user_input, view):
        self.user_input = user_input
        self.view = view

    def show_codecooler_details_action(self, users_list):
        """Show details of chosen user_input

        Parameters:
            users_list: list of codecoolers class objects
        Returns:
            None
        """
        self.view.show_codecoolers(users_list)
        message = 'Please choose index of user:'
        self.view.show_message(message)
        user_index = self.user_input.get_index_input(len(users_list))
        user = users_list[user_index]
        self.view.show_codecooler(user)

    def show_codecooler_action(self, user_role):
        """Show codecoolers and their details

        Parameters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        options = ["show details", "back"]

        if user_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecoolers(mentors)
            self.view.show_menu_option(options)
            option = self.user_input.get_option(options)

            if option == options[0]:
                self.show_codecooler_details_action(mentors)

        elif user_role == "student":
            students = Student.get_students()
            self.view.show_codecoolers(students)
            self.view.show_menu_option(options)
            option = self.user_input.get_option(options)
            if option == options[0]:
                self.show_codecooler_details_action(students)

    def add_codecooler_action(self, person_role):
        """Create and add codecooler object to class list

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """
        message = 'Please provide user data:'
        self.view.show_message(message)
        if person_role == "mentor":
            mentor = Mentor(*self.user_input.get_codecooler_data())
            mentor.add_to_mentors()
        elif person_role == "student":
            student = Student(*self.user_input.get_codecooler_data())
            student.add_to_students()

        self.view.show_message("New Codecooler added!")

    def edit_codecooler_action(self, person_role):
        """Edits codecooler object attributes

        Parmeters:
            user_role: str ("mentor" or "student")
        Returns:
            None
        """

        if person_role == "mentor":
            codecoolers = Mentor.get_mentors()
        elif person_role == "student":
            codecoolers = Student.get_students()

        self.view.show_codecoolers(codecoolers)
        index_decision = self.user_input.get_index_input(len(codecoolers))
        codecooler = codecoolers[index_decision]

        edit_options = ["Edit first name", "Edit last name",
                        "Edit e-mail", "Edit password"]
        self.view.show_menu_option(edit_options)
        edit_decision = self.user_input.get_option(edit_options)

        if edit_decision == "Edit first name":
            first_name = self.user_input.get_specific_codecooler_data("first name")
            codecooler.set_first_name(first_name)
        elif edit_decision == "Edit last name":
            last_name = self.user_input.get_specific_codecooler_data("last name")
            codecooler.set_last_name(last_name)
        elif edit_decision == "Edit password":
            password = self.user_input.get_specific_codecooler_data("password")
            codecooler.set_password(password)
        elif edit_decision == "Edit e-mail":
            email = self.user_input.get_codecooler_email()
            codecooler.set_email(email)

        self.view.show_message("Codecooler's data edited!")


    def remove_codecooler_action(self, person_role):
        """Remove codecooler object from class list

        Parameters:
            person_role: str ("mentor" or "student")
        Returns:
            None
        """
        message = 'Please choose user to remove:'
        self.view.show_message(message)
        if person_role == "mentor":
            mentors = Mentor.get_mentors()
            self.view.show_codecoolers(mentors)
            option = self.user_input.get_index_input(len(mentors))
            mentor = mentors[option]
            Mentor.remove(mentor)

        elif person_role == "student":
            students = Student.get_students()
            self.view.show_codecoolers(students)
            option = self.user_input.get_index_input(len(students))
            student = students[option]
            Student.remove(student)

        self.view.show_message("Codecooler removed!")
