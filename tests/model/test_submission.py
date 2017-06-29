import unittest
from unittest.mock import Mock

from model.assignment import Assignment
from model.codecooler import Student
from model.submission import Submission


class TestSubmission(unittest.TestCase):
    def test_if_submission_init_throws_exception_when_student_is_not_student_class_type(self):
        submission_data = ("", Mock(Assignment), "solution")
        with self.assertRaises(TypeError):
            Submission(*submission_data)

    def test_if_submission_init_throws_exception_when_assignment_is_not_assignment_class_type(self):
        submission_data = (Mock(Student), "", "solution")
        with self.assertRaises(TypeError):
            Submission(*submission_data)

    def test_if_submission_init_throws_exception_when_solution_is_empty(self):
        submission_data = (Mock(Student), Mock(Assignment), "")
        with self.assertRaises(ValueError):
            Submission(*submission_data)
