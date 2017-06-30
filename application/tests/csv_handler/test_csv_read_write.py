import unittest
from application.read_write_csv.csv_read_write import *



class TestCsvHandler(unittest.TestCase):
    incorrect_path = "incorrect_path"
    write_incorrect_path = "incorrect_path_write"

    def test_if_read_students_from_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_students_from_csv(self.incorrect_path)

    def test_if_read_attendances_from_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_attendances_from_csv(self.incorrect_path)

    def test_if_read_assignments_from_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_assignments_from_csv(self.incorrect_path)

    def test_read_submissions_from_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_submissions_from_csv(self.incorrect_path)

    def test_if_write_codecoolers_to_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            write_codecoolers_to_csv(self.write_incorrect_path)

    def test_if_write_attendance_to_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            write_attendance_to_csv(self.write_incorrect_path)

    def test_if_write_assignments_to_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_assignments_from_csv(self.write_incorrect_path)

    def test_write_assignments_to_csv_hasIncorrectFilePath_raiseFileNotFoundError(self):
        with self.assertRaises(FileNotFoundError):
            read_submissions_from_csv(self.write_incorrect_path)