from student_manager import get_grade, get_result, search_students 


def test_get_grade_A():
    assert get_grade(95) == "A"


def test_get_grade_B():
    assert get_grade(75) == "B"


def test_get_grade_C():
    assert get_grade(65) == "C"


def test_get_grade_D():
    assert get_grade(55) == "D"


def test_get_grade_F():
    assert get_grade(45) == "F"

def test_get_result_return_pass():
    assert get_result(60) == "Pass"

def test_get_result_return_fail():
    assert get_result(59) == "Fail"

def test_search_students_found():
    students = [
        {"name": "Alice", "age": 20, "score": 85, "result": "Pass", "grade": "A"},
        {"name": "Bob", "age": 22, "score": 75, "result": "Pass", "grade": "B"},
        {"name": "Charlie", "age": 21, "score": 55, "result": "Fail", "grade": "D"}
    ]
    search_name = "Alice"
    found_students = search_students(students, search_name)
    assert len(found_students) == 1
    assert found_students[0]["name"] == "Alice"

def test_search_students_not_found():
    students = [
        {"name": "Alice", "age": 20, "score": 85, "result": "Pass", "grade": "A"},
        {"name": "Bob", "age": 22, "score": 75, "result": "Pass", "grade": "B"},
        {"name": "Charlie", "age": 21, "score": 55, "result": "Fail", "grade": "D"}
    ]
    search_name = "David"
    found_students = search_students(students, search_name)
    assert len(found_students) == 0

def test_search_students_case_insensitive():
    students = [
        {"name": "Alice", "age": 20, "score": 85, "result": "Pass", "grade": "A"},
        {"name": "Bob", "age": 22, "score": 75, "result": "Pass", "grade": "B"},
        {"name": "Charlie", "age": 21, "score": 55, "result": "Fail", "grade": "D"}
    ]
    search_name = "aliCe"
    found_students = search_students(students, search_name)
    assert len(found_students) == 1
    assert found_students[0]["name"] == "Alice"

def test_search_students_multiple_matches():
    students = [
        {"name": "Alice", "age": 20, "score": 85, "result": "Pass", "grade": "A"},
        {"name": "Bob", "age": 22, "score": 75, "result": "Pass", "grade": "B"},
        {"name": "Alice", "age": 21, "score": 55, "result": "Fail", "grade": "D"}
    ]
    search_name = "Alice"
    found_students = search_students(students, search_name)
    assert len(found_students) == 2
    assert found_students[0]["age"] == 20
    assert found_students[1]["age"] == 21

