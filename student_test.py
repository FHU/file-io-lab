import student

def test_default_name():
    stud = student.Student()
    assert stud.name == ""

def test_default_lab():
    stud = student.Student()
    assert stud.lab == 0

def test_default_test():
    stud = student.Student()
    assert stud.test == 0

def test_default_final_exam():
    stud = student.Student()
    assert stud.final_exam == 0

def test_default_overall():
    stud = student.Student()
    assert stud.overall == 0

def test_default_lab():
    stud = student.Student()
    assert stud.letter_grade == ""

def test_overall_grade_A():
    stud_A = student.Student()

    stud_A.lab = 95
    stud_A.test = 94
    stud_A.final_exam = 96
    stud_A.calc_overall_grade()
    assert stud_A.overall == 95

def test_overall_grade_B():
    stud_B = student.Student()

    stud_B.lab = 85
    stud_B.test = 84
    stud_B.final_exam = 86
    stud_B.calc_overall_grade()
    assert stud_B.overall == 85

def test_overall_grade_C():
    stud_C = student.Student()

    stud_C.lab = 75
    stud_C.test = 74
    stud_C.final_exam = 76
    stud_C.calc_overall_grade()
    assert stud_C.overall == 75

def test_overall_grade_D():
    stud_D = student.Student()

    stud_D.lab = 65
    stud_D.test = 64
    stud_D.final_exam = 66
    stud_D.calc_overall_grade()
    assert stud_D.overall == 65

def test_overall_grade_F():
    stud_F = student.Student()

    stud_F.lab = 55
    stud_F.test = 54
    stud_F.final_exam = 56
    stud_F.calc_overall_grade()
    assert stud_F.overall == 55

def test_letter_grade_A():
    stud_A = student.Student()

    stud_A.lab = 95
    stud_A.test = 94
    stud_A.final_exam = 96
    stud_A.calc_overall_grade()
    stud_A.calc_letter_grade()
    assert stud_A.letter_grade == "A"

def test_letter_grade_B():
    stud = student.Student()

    stud.lab = 85
    stud.test = 84
    stud.final_exam = 86
    stud.calc_overall_grade()
    stud.calc_letter_grade()
    assert stud.letter_grade == "B"

def test_letter_grade_C():
    stud = student.Student()

    stud.lab = 75
    stud.test = 74
    stud.final_exam = 76
    stud.calc_overall_grade()
    stud.calc_letter_grade()
    assert stud.letter_grade == "C"

def test_letter_grade_D():
    stud = student.Student()

    stud.lab = 65
    stud.test = 64
    stud.final_exam = 66
    stud.calc_overall_grade()
    stud.calc_letter_grade()
    assert stud.letter_grade == "D"

def test_letter_grade_F():
    stud = student.Student()

    stud.lab = 55
    stud.test = 54
    stud.final_exam = 56
    stud.calc_overall_grade()
    stud.calc_letter_grade()
    assert stud.letter_grade == "F"