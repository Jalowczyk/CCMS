import datetime

from application.model.attendance import Attendance
from application.model.codecooler import Student


class AttendanceController:
    """
    Creates AttendanceController obj.

    Instance attributes:
    user_imput: UserInput obj
    """

    def __init__(self, user_input, view):
        """
        Creates AttendanceController obj.
        Parameters:
        user_input: UserInput obj
        view_input: View obj
        """

        self.user_input = user_input
        self.view = view

    def check_attendance_action(self):
        """
        Creates Attendance obj based on user input and adds to attendaces
        attribute (list).
        """

        students = Student.get_students()
        today_date = datetime.date.today()
        for student in students:
            self.view.show_codecooler(student)
            is_present = self.user_input.get_boolean_input()
            new_attendance = Attendance(today_date, student, is_present)
            if not any(new_attendance.get_date() == attendance.get_date() for attendance in student.get_attendance()):
                new_attendance.add_to_attendances()
                student.add_attendance(new_attendance)
            else:
                for attendance in student.get_attendance():
                     if attendance.get_date() == new_attendance.get_date():
                         attendance.set_is_present(new_attendance.get_is_present())

        self.view.show_message("There are no more students!")

    def view_attendance_action(self):

        for index, student in enumerate(Student.get_students()):
            present = 0
            for attendance in student.get_attendance():
                if attendance.get_is_present():
                    present += 1

            percent_attendance = int(100 * (present/len(student.get_attendance())))
            self.view.show_attendance(index + 1, student, percent_attendance)

        group_name = "student's"
        user_aux_menu_decision = self.user_input.get_aux_menu_input(len(Student.get_students()), group_name)

        if isinstance(user_aux_menu_decision, int):
            choosen_student = Student.get_students()[user_aux_menu_decision]
            self.view.show_attendance_details(choosen_student)
