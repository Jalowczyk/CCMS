class View:

    def show_menu_option(self, options):

        for index, option in enumerate(options):
            print("{}{} {}".format(index + 1, ".", option))

    def show_codecooler(self, codecooler):

        print("{} {}: {}".format(codecooler.get_first_name(),
                                 codecooler.get_last_name(), get_email()))

    def show_assignments(self, assignments):

        for index, assignment in enumerate(assignments):
            print("{}{} {}".format(index + 1, ".", assignment))
