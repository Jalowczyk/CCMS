class View:

    def show_menu_option(self, options):

        for index, option in enumerate(options):
            print("{}{} {}".format(index + 1, ".", option))

    
