from controller/codecooler_controller import CodecoolerController
from controller/attendance_controller import AttendanceController
from controller/submission_controller import SubmissionController
from view/view import View

class Menu:
    """
    Creates Menu object.

    Class attributes:
    options: list

    Instance attributes:
    logged_user: Codecooler obj
    view: View obj
    user_input: UserInput obj
    codecooler_controller: CodecoolerController obj
    attendance_controller: AttendanceController obj
    submission_controller: SubmissionController obj
    assignment_controller: AssignmentController obj
    """
    options = ["log out"]
