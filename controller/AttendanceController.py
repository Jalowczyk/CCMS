from model.attendance import Attendance


class AttendanceController:
    """
    Creates AttendanceController obj.

    Instance attributes:
    user_imput: UserInput obj
    """

    def __init__(self, user_input):
        """
        Creates AttendanceController obj.
        Parameters:
        user_input: UserInput obj
        """

        self.user_input = user_input

    def check_attendance_action(self):
        """
        Creates Attendance obj based on user input.
        """
        date, student, is_present = self.user_input.get_attendance_input()
        attendance = Attendance(date, student, is_present)
        attendance.add_to_attendances()
