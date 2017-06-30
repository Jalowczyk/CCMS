import datetime
import unittest
import unittest.mock

from application.model.attendance import Attendance


class TestAttendance(unittest.TestCase):
    correct_date = datetime.date(2017, 11, 27)
    student = unittest.mock
    isPresent = True

    def test___init__IfEmptyDate_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Attendance(None, self.student, self.isPresent)

    def test___init__IfEmptyStudent_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Attendance(self.correct_date, None, self.isPresent)

    def test___init__IfEmptyIsPresent_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Attendance(self.correct_date, self.student, None)

    def test_addToAddendances_AttendancesListIncrements(self):
        attendance = Attendance(self.correct_date, self.student, self.isPresent)
        previous_attendances_lenght = len(Attendance.get_attendances())
        attendance.add_to_attendances()
        self.assertEqual(len(Attendance.get_attendances()), previous_attendances_lenght + 1)
