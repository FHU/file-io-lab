import main
import csv
import random
import student

def test_lab_avg():
    assert main.lab_avg == 37

def test_test_avg():
    assert main.test_avg == 41

def test_final_exam_avg():
    assert main.final_exam_avg == 53

def test_overall_avg():
    assert main.overall_avg == 44

def test_students_list():
    with open('file_io_lab_data.csv', 'r') as csvfile:
        lines = len(csvfile.readlines())
        assert len(main.students) == lines -1

def test_isinstance():
    index = random.randrange(51)
    stud = main.students[index]
    assert isinstance(stud, student.Student) == True