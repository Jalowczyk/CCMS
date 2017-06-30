import unittest
from unittest.mock import Mock

from application.model.assignment import Assignment
from application.model.codecooler import Student
from application.model.submission import Submission


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

    def test_if_add_to_assignments_adds_assignment_to_class_list(self):
        assignment_data = ("title", "description", 10)
        assignment = Assignment(*assignment_data)
        assignment_desired_list = [assignment]
        assignment.add_to_assignments()
        self.assertListEqual(assignment_desired_list, Assignment.get_assignments())

    def test_if_add_submission_adds_submission_to_list(self):
        assignment_data = ("title", "description", 10)
        assignment = Assignment(*assignment_data)
        submission_mock = Mock(Submission(Mock(Student), Mock(Assignment), "solution"))
        submission_desired_list = [submission_mock]
        assignment.add_submission(submission_mock)
        self.assertListEqual(submission_desired_list, assignment.get_submissions())

    def test_if_get_title_returns_proper_value(self):
        assignment_data = ("title", "description", 10)
        assignment = Assignment(*assignment_data)
        self.assertEqual(assignment.get_title(), "title")

    def test_if_get_description_returns_proper_value(self):
        assignment_data = ("title", "description", 10)
        assignment = Assignment(*assignment_data)
        self.assertEqual(assignment.get_description(), "description")

    def test_if_get_max_grade_returns_proper_value(self):
        assignment_data = ("title", "description", 10)
        assignment = Assignment(*assignment_data)
        self.assertEqual(assignment.get_max_grade(), 10)
