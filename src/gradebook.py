"""Grade Book Manager - a CLI program."""

from helpers import (
    add_student, find_student, add_grade, get_student_average,
    get_all_subjects, get_top_student, get_lowest_student
)


def show_menu():
    print("\n===== GRADE BOOK MANAGER =====")
    print("1. Add student")
    print("2. Add grade")
    print("3. Show student report")
    print("4. Show all students (sorted by average)")
    print("5. Top and lowest student")
    print("6. Search student")
    print("7. List unique subjects")
    print("8. Quit")


def display_student_report(student):
    print("\n" + "=" * 40)
    print(f"Student: {student['name']}")
    print(f"ID: {student['id']}")
    if not student["grades"]:
        print("No grades recorded yet.")
    else:
        print("Grades:")
        for subject, grade in student["grades"].items():
            print(f"  {subject}: {grade}")
        print(f"Average: {get_student_average(student):.2f}")
    print("=" * 40)


def display_all_students(students):
    if not students:
        print("No students in the gradebook.")
        return
    print("\n" + "=" * 50)
    print("GRADEBOOK REPORT (sorted by average, highest first)")
    print("=" * 50)
    sorted_students = sorted(students, key=get_student_average, reverse=True)
    for student in sorted_students:
        print(f"{student['name']} (ID: {student['id']}) - "
              f"Average: {get_student_average(student):.2f}")
    print("=" * 50)


def get_int_input(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number.")


def get_grade_input(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if 0 <= value <= 100:
                return value
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def main():
    students = []
    keep_going = True
    while keep_going:
        show_menu()
        choice = input("Choose 1-8: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            student_id = get_int_input("Student ID: ")
            add_student(students, name, student_id)
            
        elif choice == "2":
            name = input("Student name: ").strip()
            subject = input("Subject: ").strip().lower()
            grade = get_grade_input("Grade (0-100): ")
            add_grade(students, name, subject, grade)
            
        elif choice == "3":
            name = input("Student name: ").strip()
            student = find_student(students, name)
            if student:
                display_student_report(student)
            else:
                print(f"Student '{name}' not found.")
                
        elif choice == "4":
            display_all_students(students)
            
        elif choice == "5":
            top = get_top_student(students)
            low = get_lowest_student(students)
            if top and low:
                print(f"Top: {top['name']} ({get_student_average(top):.2f})")
                print(f"Lowest: {low['name']} ({get_student_average(low):.2f})")
            else:
                print("No students in the gradebook.")
                
        elif choice == "6":
            name = input("Search name: ").strip()
            matches = [s for s in students if name.lower() in s["name"].lower()]
            if matches:
                for s in matches:
                    print(f"Found: {s['name']} (ID: {s['id']})")
            else:
                print("No matching students.")
                
        elif choice == "7":
            subjects = get_all_subjects(students)
            if subjects:
                print("Unique subjects:", ", ".join(sorted(subjects)))
            else:
                print("No subjects recorded yet.")
                
        elif choice == "8":
            keep_going = False
            print("Goodbye!")
            
        else:
            print("Invalid choice. Enter 1-8.")


main()
