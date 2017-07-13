from application.model.assignment import Assignment


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
        if data is None:
            return
        assignment = Assignment(*data)
        assignment.add_to_assignments()

        self.view.show_message("New assignment added!")
        self.user_input.press_enter_to_continue()

    def get_assignment(self, assignments):
        """Gets assignment object form class list

        Returns:
            assignment: list of Assignment object
        """
        group_name = "assignment's"
        index = self.user_input.get_index_input(len(assignments), group_name)
        return assignments[index]

    def show_assignments(self):
        """Show details of assignment object

        Returns:
            None
        """
        assignments = Assignment.get_assignments_list()
        self.view.show_assignments(assignments)
        group_name = "assignment's"
        user_aux_menu_decision = self.user_input.get_aux_menu_input(len(assignments), group_name)
        self.view.clear()
        if isinstance(user_aux_menu_decision, int):
            choosen_assignment = assignments[user_aux_menu_decision]
            self.view.show_assignment_details(choosen_assignment)
        self.user_input.press_enter_to_continue()
