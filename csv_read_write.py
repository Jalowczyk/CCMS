import csv
from datetime import date
from model.attendance import *
from model.codecooler import *
from model.assignment import *
from model.submission import *


def read_students_from_csv(file_name):
    '''
    Create models and fill class lists with data from csv files at the begining of program

    Raises *FileNotFoundError* if a file doesn't exist.

    Every item is written to a separate line in the following format:
    `Role|first name|last name|email|password`

    Args:
        file_name (str): name of the file

    Returns:
        void
    '''
    try:
        codecooler_roles = {'Student': Student,
                            'Staff': Staff,
                            'Mentor': Mentor,
                            'Manager': Manager}

        with open(file_name, "r") as file:
            lines = file.readlines()
        codecoolers_list = [element.replace("\n", "").split("|") for element in lines]

        for codecooler in codecoolers_list:
            role = codecooler[0]
            first_name = codecooler[1]
            last_name = codecooler[2]
            email = codecooler[3]
            password = codecooler[4]
            new_codecooler = codecooler_roles[role](first_name, last_name, email, password)

            if type(new_codecooler) is Student:
                new_codecooler.add_to_students()
            elif type(new_codecooler) is Staff:
                new_codecooler.add_to_staff()
            elif type(new_codecooler) is Mentor:
                new_codecooler.add_to_mentors()
            elif type(new_codecooler) is Manager:
                new_codecooler.add_to_managers()

    except FileNotFoundError:
        raise FileNotFoundError('File' + file_name + 'doesn\'t exist')


def write_codecoolers_to_csv(file_name):
    '''
    Save codecoolers data from classes lists at the end of the program.

    Every item is written to a separate line in the following format:
    `Role|first name|last name|email|password`

    Args:
        file_name (str): name of the file

    Returns:
        void
    '''
    codecoolers_list = (Student.get_students()
                        + Manager.get_managers()
                        + Mentor.get_mentors()
                        + Staff.get_staff())
    with open(file_name, "w") as file:
        for codecooler in codecoolers_list:
            codecooler_details = list(codecooler.__dict__.values())
            row = [codecooler.__class__.__name__]
            [row.append(detail) for detail in codecooler_details[0:4]]
            file.write('|'.join(row) + '\n')


def read_attendances_from_csv(file_name):
    '''
    Create models and fill Attendance class list with data from csv files at the begining of program.

    Raises *FileNotFoundError* if a file doesn't exist.

    Every item is written to a separate line in the following format:
    `email|date|X` X = 0 for absent, X = 1 for present

    Args:
        file_name (str): name of the file

    Returns:
        void
    '''
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        attendances_list = [element.replace("\n", "").split("|") for element in lines]

        for attendance in attendances_list:
            date_to_write = attendance[0].split('-')
            year = int(date_to_write[0])
            month = int(date_to_write[1])
            day = int(date_to_write[2])
            date_to_write = date(year, month, day)

            is_present = int(attendance[2])

            email = attendance[1]

            students_list = Student.get_students()
            for student in students_list:
                if student.email == email:
                    new_attendance = Attendance(date_to_write, student, is_present)
                    new_attendance.add_to_attendances()
                    student.add_attendance(new_attendance)

    except FileNotFoundError:
        raise FileNotFoundError('File' + file_name + 'doesn\'t exist')


def write_attendance_to_csv(file_name):
    '''
    Save attendance data from class list at the end of the program.

    Every item is written to a separate line in the following format:
    `email|date|is_present` is_present = 0 for absent, is_present = 1 for present

    Args:
        file_name (str): name of the file
        attendances_list (list of :obj: 'Attendance'): list of attendances objects

    Returns:
        void
    '''
    attendances_list = Attendance.get_attendance()
    with open(file_name, "w") as file:
        for attendance in attendances_list:
            attendance_details = list(attendance.__dict__.values())
            student_details = list(attendance_details[1].__dict__.values())

            date = attendance_details[0]
            email = student_details[2]
            is_present = str(attendance_details[2])

            row = [str(date), email, is_present]
            file.write('|'.join(row) + '\n')
