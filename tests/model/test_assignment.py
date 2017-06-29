import unittest
from model.assignment import Assignment
from model.submission import Submission


class TestAssignment(unittest.TestCase):
    def test_if_assignment_init_throws_exception_when_title_empty(self):
        assignment_data = ("", "description", 10)
        with self.assertRaises(ValueError):
            Assignment(*assignment_data)

    def test_if_assignment_init_throws_exception_when_description_empty(self):
        assignment_data = ("title", "", 10)
        with self.assertRaises(ValueError):
            Assignment(*assignment_data)

    def test_if_assignment_init_throws_exception_when_max_grade_LT0(self):
        assignment_data = ("title", "", -1)
        with self.assertRaises(ValueError):
            Assignment(*assignment_data)

    def test_if_assignment_init_throws_exception_when_max_grade_is_not_numeric(self):
        assignment_data = ("title", "", "string")
        with self.assertRaises(ValueError):
            Assignment(*assignment_data)
