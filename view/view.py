class View:

    def show_menu_option(self, options):

        for index, option in enumerate(options):
            print("{}{} {}".format(index + 1, ".", option))

    def view_codecooler(self, codecooler):

        print("{} {}: {}".format(codecooler.get_first_name(), codecooler.get_last_name(),
                        get_email()))
