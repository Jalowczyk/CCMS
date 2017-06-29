from model.assignment import Assignment


class AssignmentController:
    """Represents  AssignmentController objects

    instance attributes:
        user_input: objects of UserInput class
        view: objects of View class
    """

    def __init__(self, user_input, view):
        """Instance Initializer"""
        self.user_input = user_input
        self.view = view

    def add_assignment_action(self):
        """Add Assignment object

        Returns:
            None
        """
        data = self.user_input.get_assignment_data()
        assignment = Assignment(*data)
        assignment.add_to_assignments()

    def get_assignment(self, assignments):
        """Gets assignment object form class list

        Returns:
            assignment: list of Assignment object
        """
        index = self.user_input.get_index_input(len(assignments))
        return assignments[index]

    def show_assignments_details(self):
        """Show details of assignment object

        Returns:
            None
        """
        options = ['view details', 'back']
        assignments = Assignment.get_assignments_list()
        self.view.show_assignments(assignments)
        self.view.show_menu_option(options)
        option = self.user_input.get_menu_input(options)
        if option == options[0]:
            assignment = self.get_assignment(assignments)
            self.view.show_assignment_details(assignment)
