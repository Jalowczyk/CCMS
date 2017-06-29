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

    def test_if_set_grade_sets_value(self):
        submission_data = (Mock(Student), Mock(Assignment), "solution")
        submission = Submission(*submission_data)
        grade = 10
        submission.set_grade(grade)
        self.assertEqual(submission.get_grade(), grade)

    def test_if_set_grade_throws_exception_when_grade_is_not_numeric(self):
        submission_data = (Mock(Student), Mock(Assignment), "solution")
        submission = Submission(*submission_data)
        grade = "ab"
        with self.assertRaises(TypeError):
            submission.set_grade(grade)

    def test_if_set_grade_throws_exception_when_grade_is_LT0(self):
        submission_data = (Mock(Student), Mock(Assignment), "solution")
        submission = Submission(*submission_data)
        grade = -1
        with self.assertRaises(ValueError):
            submission.set_grade(grade)

    def test_if_get_assignment_returns_proper_value(self):
        assignment = Mock(Assignment)
        submission_data = (Mock(Student), assignment, "solution")
        submission = Submission(*submission_data)
        self.assertEqual(assignment, submission.get_assignment())

    def test_if_get_is_graded_returns_proper_value(self):
        assignment = Mock(Assignment)
        submission_data = (Mock(Student), assignment, "solution")
        submission = Submission(*submission_data)
        submission.is_graded = True
        self.assertTrue(submission.get_is_graded())

    def test_if_get_solution_returns_proper_value(self):
        solution = "solution"
        submission_data = (Mock(Student), Mock(Assignment), solution)
        submission = Submission(*submission_data)
        self.assertEqual(solution, submission.get_solution())
