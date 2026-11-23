"""Helper functions for the gradebook."""


def add_student(students, name, student_id):
    """Add a new student. Returns True if added, False if ID exists."""
    for student in students:
        if student["id"] == student_id:
            print(f"Error: ID {student_id} already exists.")
            return False
    students.append({"name": name, "id": student_id, "grades": {}})
    print(f"Added student: {name} (ID: {student_id})")
    return True


def find_student(students, name):
    """Find a student by name (case-insensitive). Returns dict or None."""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def add_grade(students, student_name, subject, grade):
    """Add/update a grade for a student. Returns True on success."""
    student = find_student(students, student_name)
    if student is None:
        print(f"Student '{student_name}' not found.")
        return False
    if grade < 0 or grade > 100:
        print("Error: grade must be between 0 and 100.")
        return False
    student["grades"][subject] = grade
    print(f"Added {subject} grade ({grade}) for {student['name']}")
    return True


def calculate_average(grades):
    """Average of a list of numbers. Returns 0 if empty."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_student_average(student):
    """Average across a student's grade values. Returns 0 if no grades."""
    if not student["grades"]:
        return 0
    return calculate_average(list(student["grades"].values()))


def get_all_subjects(students):
    """Return a set of every subject any student has a grade in."""
    subjects = set()
    for student in students:
        subjects.update(student["grades"].keys())
    return subjects


def get_top_student(students):
    """Return the student dict with the highest average, or None."""
    if not students:
        return None
    return max(students, key=get_student_average)


def get_lowest_student(students):
    """Return the student dict with the lowest average, or None."""
    if not students:
        return None
    return min(students, key=get_student_average)
