import App

def test_exercice1():
    assert "Charlie" in App.students
    assert App.students.get("Eve", 0) == 0

def test_exercice2():
    assert "Python" in App.languages
    assert "C++" not in App.languages

def test_exercice3():
    assert "JavaScript" in App.skills_candidate1
