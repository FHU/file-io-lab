import student

def test_default_student_name():
    stud= student.Student("Lisa", 95, 94, 96)
    assert stud.name == "Lisa"

def test_default_student_lab():
    stud= student.Student("Lisa", 95, 94, 96)
    assert stud.lab == 95

def test_default_student_tests():
    stud= student.Student("Lisa", 95, 94, 96)
    assert stud.tests == 94

def test_default_student_final():
    stud= student.Student("Lisa", 95, 94, 96)
    assert stud.final == 96


def test_overall_grade_A():
    stud_A = student.Student("Lisa", 95, 94, 96)
    assert stud_A.overall == 95

def test_overall_letter_A():
    stud_A = student.Student("Lisa", 95, 94, 96)
    assert stud_A.letter_grade == "A"

def test_overall_grade_B():
    stud_B = student.Student("Lisa", 85, 84, 86)
    assert stud_B.overall == 85

def test_overall_letter_B():
    stud_B = student.Student("Lisa", 85, 84, 86)
    assert stud_B.letter_grade == "B"

def test_overall_grade_C():
    stud_C = student.Student("Lisa", 75, 74, 76)
    assert stud_C.overall== 75

def test_overall_letter_C():
    stud_C = student.Student("Lisa", 75, 74, 76)
    assert stud_C.letter_grade == "C"

def test_overall_grade_D():
    stud_D = student.Student("Lisa", 65, 64,66)
    assert stud_D.overall == 65

def test_overall_letter_D():
    stud_D = student.Student("Lisa", 65, 64,66)
    assert stud_D.letter_grade == "D"

def test_overall_grade_F():
    stud_F = student.Student("Lisa", 55, 54, 56)
    assert stud_F.overall== 55

def test_overall_letter_F():
    stud_F = student.Student("Lisa", 55, 54, 56)
    assert stud_F.letter_grade == "F"
