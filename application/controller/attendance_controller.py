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
            attendance = Attendance(today_date, student, is_present)
            attendance.add_to_attendances()
            student.add_attendance(attendance)