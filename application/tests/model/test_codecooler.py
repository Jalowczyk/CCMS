import unittest
import unittest.mock

from application.model.codecooler import *


class TestCodecooler(unittest.TestCase):
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

    def test_Mentor_addToMentors_mentorsListIncrements(self):
        first_length = len(Mentor.get_mentors())
        mentor = Mentor("asdf", "asdf", "asdf@asdf.pl", "asdf")
        mentor.add_to_mentors()
        self.assertEqual(len(Mentor.get_mentors()), first_length + 1)

    def test_Staff_addToStaffs_addsStaffObjectToStaffList(self):
        staff = Staff("asdf", "asdf", "asdf@asdf.pl", "asdf")
        staff.add_to_staff()
        self.assertEqual(Staff.get_staff()[-1], staff)

    def test_Staff_addToStaff_staffListIncrements(self):
        first_length = len(Staff.get_staff())
        staff = Staff("asdf", "asdf", "asdf@asdf.pl", "asdf")
        staff.add_to_staff()
        self.assertEqual(len(Staff.get_staff()), first_length + 1)

    def test_Manager_addToManagers_addsManagerObjectToManagerList(self):
        manager = Manager("asdf", "asdf", "asdf@asdf.pl", "asdf")
        manager.add_to_managers()
        self.assertEqual(Manager.get_managers()()[-1], manager)

    def test_Manager_addToManagers_ManagerListIncrements(self):
        first_length = len(Manager.get_managers())
        manager = Manager("asdf", "asdf", "asdf@asdf.pl", "asdf")
        manager.add_to_managers()
        self.assertEqual(len(Manager.get_managers()), first_length + 1)

    def test_Codecooler_getFirstName_returnCorrectName(self):
        first_name = "Name"
        codecooler = Codecooler(first_name, "lastname", "email@email.pl", "password")
        self.assertEqual(codecooler.get_first_name(), first_name)

    def test_Codecooler_getLastName_returnCorrectName(self):
        last_name = "Name"
        codecooler = Codecooler("firstname", last_name, "email@email.pl", "password")
        self.assertEqual(codecooler.get_last_name(), last_name)

    def test_Codecooler_getMail_returnCorrectMail(self):
        mail = "mail@mail.pl"
        codecooler = Codecooler("firstname", "last_name", mail, "password")
        self.assertEqual(codecooler.get_email(), mail)

    def test_Codecooler_getPassword_returnCorrectPassword(self):
        password = "password"
        codecooler = Codecooler("firstname", "last_name", "mail@mail.pl", password)
        self.assertEqual(codecooler.get_password(), password)

    def test_Codecooler_setFirstName_returnCorrectName(self):
        codecooler = Codecooler("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        first_name = "New first name"
        codecooler.set_first_name(first_name)
        self.assertEqual(codecooler.get_first_name(), first_name)

    def test_Codecooler_setLastName_returnCorrectName(self):
        codecooler = Codecooler("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        last_name = "New last name"
        codecooler.set_last_name(last_name)
        self.assertEqual(codecooler.get_last_name(), last_name)

    def test_Codecooler_setMail_returnCorrectMail(self):
        codecooler = Codecooler("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        mail = "mail@mail.pl"
        codecooler.set_email(mail)
        self.assertEqual(codecooler.get_email(), mail)

    def test_Codecooler_setPassword_returnCorrectPassword(self):
        codecooler = Codecooler("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        password = "newpassword"
        codecooler.set_password(password)
        self.assertEqual(codecooler.get_password(), password)

    def test_StudentRemove_StudentNotInStudentList(self):
        student = Student("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        student.add_to_students()
        student.remove()
        self.assertFalse(any([stud == student for stud in Student.get_students()]))

    def test_MentorRemove_MentorNotInMentorList(self):
        mentor_to_remove = Mentor("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        mentor_to_remove.add_to_mentors()
        mentor_to_remove.remove()
        self.assertFalse(any([mentor == mentor_to_remove for mentor in Mentor.get_mentors()]))

    def test_Student_afterInit_hasEmptyAttendanceList(self):
        student = Student("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        self.assertEqual(len(student.get_attendance()), 0)

    def test_Student_afterInit_hasEmptySubmissionList(self):
        student = Student("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        self.assertEqual(len(student.get_submissions()), 0)

    def test_StudentAddSubmission_SubmissionListIncrements(self):
        student = Student("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        previous_submissions_length = len(student.get_submissions())
        submission = unittest.mock.Mock()
        student.add_submission(submission)
        self.assertEqual(len(student.get_submissions()), previous_submissions_length + 1)

    def test_StudentAddAttendance_AttendanceListIncrements(self):
        student = Student("Old first name", "Old last name", "old@mail.com", "Oldpassword")
        previous_attendances_length = len(student.get_attendance())
        attendance = unittest.mock.Mock()
        student.add_attendance(attendance)
        self.assertEqual(len(student.get_attendance()), previous_attendances_length + 1)
