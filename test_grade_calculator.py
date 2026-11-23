from grade_calculator import average, grade, is_pass, feedback

def test_average():
    assert average([80, 90, 70]) == 80

def test_grade_A():
    assert grade(95) == "A"

def test_grade_B():
    assert grade(85) == "B"

def test_grade_C():
    assert grade(75) == "C"

def test_grade_F():
    assert grade(40) == "F"

def test_pass():
    assert is_pass([80, 75, 90]) == True

def test_fail():
    assert is_pass([80, 30, 90]) == False

def test_feedback_excellent():
    assert feedback(90) == "Excellent performance!"