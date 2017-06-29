class AssignmentController:

    def __init__(self, user_input, view):
        self.user_input = user_input
        self.view = view

    def add_assignment_action(self):
        data = self.user_input.get_assignment_data()
        assignment = Assignment(data)
        assignment.add_to_assignments()

    def show_assignments(self):
        assignments = Assignment.get_assignments_list()
        self.view.show_assignments(assignments)
        return assignments

    def get_assignment(self, assignments):
        index = self.assignment_input.get_index_input(len(assignments))
        assignment = assignments[index]
        return assignment

    def show_assignments_details(self):
        options = ['view details', 'back']
        assignments = show_assignments
        self.view.show_menu_option(options)
        option = self.input.get_menu_input(options)
        if option == options[0]:
            assignment = self.get_assignment(assignments)
            self.view.show.assignment_details(assignment)
