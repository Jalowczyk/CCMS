from application.model.assignment import *
from application.model.attendance import *
from application.model.codecooler import *
from application.model.submission import *
from datetime import date


class CsvHandling:
    """
    Simply - csv handling.
    """
    @staticmethod
    def csv_create_if_non_exist():
        """
        Method is started when program cannot find csv files - then creating them.
        """
        with open("application/data/assignments.csv", "w") as my_poor_empty_csv:
            pass
        with open("application/data/attendance.csv", "w") as my_poor_empty_csv:
            pass
        with open("application/data/codecoolers_data.csv", "w") as my_poor_empty_csv:
            pass
        with open("application/data/submissions.csv", "w") as my_poor_empty_csv:
            pass

        print('This is the first run of the program. Default values of manager account are:\n\
               First name: Admin\n\
               Last_name: Adminsky\n\
               email: admin.adminsky@cc.pl\n\
               password: dupa\n\
               You can change this date later.\n')

        new_manager = Manager('Admin', 'Adminsky', 'admin.adminsky@cc.pl', 'dupa')
        new_manager.add_to_managers()

    @staticmethod
    def read_students_from_csv(file_name):
        """
        Create models and fill class lists with data from csv files at the begining of program

        Raises *FileNotFoundError* if a file doesn't exist.

        Every item is written to a separate line in the following format:
        `Role|first name|last name|email|password`

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        try:
            codecooler_roles = {'Student': Student,
                                'Staff': Staff,
                                'Mentor': Mentor,
                                'Manager': Manager}

            with open(file_name, "r") as file:
                lines = file.readlines()
            codecoolers_list = [element.replace("\n", "").split("|") for element in lines]

            for codecooler in codecoolers_list:
                role = codecooler[0]
                first_name = codecooler[1]
                last_name = codecooler[2]
                email = codecooler[3]
                password = codecooler[4]
                new_codecooler = codecooler_roles[role](first_name, last_name, email, password)

                if type(new_codecooler) is Student:
                    new_codecooler.add_to_students()
                elif type(new_codecooler) is Staff:
                    new_codecooler.add_to_staff()
                elif type(new_codecooler) is Mentor:
                    new_codecooler.add_to_mentors()
                elif type(new_codecooler) is Manager:
                    new_codecooler.add_to_managers()

        except FileNotFoundError:
            raise FileNotFoundError('File' + file_name + 'doesn\'t exist')

    @staticmethod
    def write_codecoolers_to_csv(file_name):
        """
        Save codecoolers data from classes lists at the end of the program.

        Every item is written to a separate line in the following format:
        `Role|first name|last name|email|password`

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        codecoolers_list = (Student.get_students()
                            + Manager.get_managers()
                            + Mentor.get_mentors()
                            + Staff.get_staff())
        with open(file_name, "w") as file:
            for codecooler in codecoolers_list:
                codecooler_class_name = codecooler.__class__.__name__
                codecooler_first_name = codecooler.get_first_name()
                codecooler_last_name = codecooler.get_last_name()
                codecooler_email = codecooler.get_email()
                codecooler_password = codecooler.get_password()
                codecooler_data = [codecooler_class_name, codecooler_first_name, codecooler_last_name, codecooler_email,
                                   codecooler_password]
                file.write('|'.join(codecooler_data) + '\n')

    @staticmethod
    def read_attendances_from_csv(file_name):
        """
        Create models and fill Attendance class list with data from csv files at the begining of program.

        Raises *FileNotFoundError* if a file doesn't exist.

        Every item is written to a separate line in the following format:
        `email|date|X` X = 0 for absent, X = 1 for present

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            attendances_list = [element.replace("\n", "").split("|") for element in lines]

            for attendance in attendances_list:
                date_to_write = attendance[0].split('-')
                year = int(date_to_write[0])
                month = int(date_to_write[1])
                day = int(date_to_write[2])
                date_to_write = date(year, month, day)

                is_present = bool(attendance[2])

                email = attendance[1]

                students_list = Student.get_students()
                for student in students_list:
                    if student.email == email:
                        new_attendance = Attendance(date_to_write, student, is_present)
                        new_attendance.add_to_attendances()
                        student.add_attendance(new_attendance)

        except FileNotFoundError:
            raise FileNotFoundError('File' + file_name + 'doesn\'t exist')

    @staticmethod
    def write_attendance_to_csv(file_name):
        """
        Save attendance data from class list at the end of the program.

        Every item is written to a separate line in the following format:
        `email|date|is_present` is_present = 0 for absent, is_present = 1 for present

        Args:
            file_name (str): name of the file
            attendances_list (list of :obj: 'Attendance'): list of attendances objects

        Returns:
            void
        """
        attendances_list = Attendance.get_attendances()
        with open(file_name, "w") as file:
            for attendance in attendances_list:
                date = attendance.get_date()
                student_email = attendance.get_student().get_email()
                is_present = attendance.get_is_present()
                attendance_data = [str(date), student_email, str(is_present)]
                file.write('|'.join(attendance_data) + '\n')

    @staticmethod
    def read_assignments_from_csv(file_name):
        """
        Create models and fill Assignment class list with data from csv files at the begining of program.

        Raises *FileNotFoundError* if a file doesn't exist.

        Every item is written to a separate line in the following format:
        `title|description|max_grade'

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            assignments_list = [element.replace("\n", "").split("|") for element in lines]
            for assignment in assignments_list:
                title = assignment[0]
                description = assignment[1]
                max_grade = int(assignment[2])
                new_assignment = Assignment(title, description, max_grade)
                new_assignment.add_to_assignments()

        except FileNotFoundError:
            raise FileNotFoundError('File' + file_name + 'doesn\'t exist')

    @staticmethod
    def write_assignments_to_csv(file_name):
        """
        Save attendance data from class list at the end of the program.

        Every item is written to a separate line in the following format:
        `title|description|max_grade'

        Args:
            file_name (str): name of the file
        Returns:
            void
        """
        assignments_list = Assignment.get_assignments()
        with open(file_name, "w") as file:
            for assignment in assignments_list:
                title = assignment.get_title()
                description = assignment.get_description()
                max_grade = assignment.get_max_grade()
                assignment_data = [title, description, str(max_grade)]
                file.write('|'.join(assignment_data) + '\n')

    @staticmethod
    def read_submissions_from_csv(file_name):
        """
        Create models and fill Assigment Submission class list with data from csv files at the begining of program.

        Raises *FileNotFoundError* if a file doesn't exist.

        `assignment_title|student_email|solution|is_graded|grade'
            str               str         str   True/False  None/int

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
            submissions_list = [element.replace("\n", "").split("|") for element in lines]

            for submission in submissions_list:
                assignment_title = submission[0]
                student_mail = submission[1]
                solution = submission[2]

                if submission[3] == 'True':
                    is_graded = True
                else:
                    is_graded = False

                if submission[4] == 'None':
                    grade = None
                else:
                    grade = int(submission[4])

                assignment_list = Assignment.get_assignments()
                students_list = Student.get_students()
                for assignment in assignment_list:
                    if assignment.title == assignment_title:
                        for student in students_list:
                            if student.email == student_mail:
                                new_submission = Submission(student, assignment, solution)
                                new_submission.set_is_graded(is_graded)
                                new_submission.set_grade(grade)
                                assignment.add_submission(new_submission)
                                student.add_submission(new_submission)

        except FileNotFoundError:
            raise FileNotFoundError('File' + file_name + 'doesn\'t exist')

    @staticmethod
    def write_submissions_to_csv(file_name):
        """
        Save submissions data from list from class Assignment at the end of the program.

        Every item is written to a separate line in the following format:
        `assignment_title|student_email|solution|is_graded|grade'
            str               str         str   True/False  None/int

        Args:
            file_name (str): name of the file

        Returns:
            void
        """
        assignment_list = Assignment.get_assignments()

        with open(file_name, "w") as file:
            for assignment in assignment_list:
                submission_list = assignment.get_submissions()
                for submission in submission_list:
                    assignment_title = submission.get_assignment().get_title()
                    student_email = submission.get_student().get_email()
                    solution = submission.get_solution()
                    is_graded = submission.get_is_graded()
                    grade = submission.get_grade()
                    solution_data = [assignment_title, student_email, solution, str(is_graded), str(grade)]
                    file.write('|'.join(solution_data) + '\n')
