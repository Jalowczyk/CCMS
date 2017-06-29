from unittest import TestCase

from model.codecooler import Codecooler, Mentor, Student


class TestCodecooler(TestCase):
    def test___init__IfEmptyFirstname_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Codecooler("", "asdf", "a@b.pl", "asdf")

    def test___init__IfEmptyLastname_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Codecooler("asdf", "", "a@b.pl", "asdf")

    def test___init__IfEmptyEmail_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Codecooler("asdf", "asdf", "", "asdf")

    def test___init__IfEmptyPassword_RaiseValueError(self):
        with self.assertRaises(ValueError):
            Codecooler("asdf", "asdf", "a@b.pl", "")

    def test___init__IfIncorrectMail_RaiseValueError(self):
        incorrect_mailes = ["asdf", "asdf@asdf", "asdf@asdf@asdf.pl", "$$$asdf@asdf.pl", "asdf@asdf."]
        for incorrect_mail in incorrect_mailes:
            with self.assertRaises(ValueError):
                Codecooler("asdf", "asdf", incorrect_mail, "asdf")


    def test_Mentor_getMentors_returnsList(self):
        mentors = Mentor.get_mentors()
        self.assertEqual(type(mentors), list)

    def test_Student_getStudents_returnsList(self):
        students = Student.get_students()
        self.assertEqual(type(students), list)

    def test_Student_addToStudents_addsStudentObjectToStudentList(self):
        student = Student("asdf", "asdf", "asdf@asdf.pl", "asdf")
        student.add_to_students()
        self.assertEqual(Student.get_students()[-1], student)

    def test_Student_addToStudents_studentsListIncrements(self):
        first_length = len(Student.get_students())
        student = Student("asdf", "asdf", "asdf@asdf.pl", "asdf")
        student.add_to_students()
        self.assertEqual(len(Student.get_students()), first_length + 1)

    def test_Mentor_addToMentor_addsMentorObjectToMentorList(self):
        mentor = Mentor("asdf", "asdf", "asdf@asdf.pl", "asdf")
        mentor.add_to_mentors()
        self.assertEqual(Mentor.get_mentors()[-1], mentor)

    def test_Mentor_addToMentors_studentsListIncrements(self):
        first_length = len(Mentor.get_mentors())
        mentor = Mentor("asdf", "asdf", "asdf@asdf.pl", "asdf")
        mentor.add_to_mentors()
        self.assertEqual(len(Mentor.get_mentors()), first_length + 1)