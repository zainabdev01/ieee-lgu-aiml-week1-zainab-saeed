"""
Student Grade & Attendance Tracker
IEEE LGU AI/ML Cohort One - Week 1 Assignment (Option 2)
Author: Zainab Saeed

Collects a student's details, subject marks, and attendance data,
then prints a clean report card showing average, letter grade,
attendance rate, and exam eligibility status.
"""


def get_non_empty_string(prompt):
    """Keep asking until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_valid_number(prompt, minimum=None, maximum=None, number_type=float):
    """Keep asking until the user enters a valid number within an optional range."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = number_type(raw_value)
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value cannot be less than {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Value cannot be more than {maximum}.")
            continue

        return value


def collect_student_info():
    """Collect the student's name and roll number."""
    name = get_non_empty_string("Enter student name: ")
    roll_number = get_non_empty_string("Enter roll number: ")
    return name, roll_number


def collect_subject_marks():
    """Ask for marks in at least 3 subjects and return them as a dictionary."""
    subjects = {}
    num_subjects = int(get_valid_number(
        "How many subjects do you want to enter (minimum 3)? ",
        minimum=3, number_type=int
    ))

    for i in range(1, num_subjects + 1):
        subject_name = get_non_empty_string(f"Enter name of subject {i}: ")
        marks = get_valid_number(
            f"Enter marks for {subject_name} (0-100): ",
            minimum=0, maximum=100
        )
        subjects[subject_name] = marks

    return subjects


def calculate_average(subjects):
    """Calculate the average marks across all subjects."""
    return sum(subjects.values()) / len(subjects)


def assign_grade(average):
    """Return a letter grade based on the average marks."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F (Fail)"


def collect_attendance():
    """Ask for total classes and classes attended, then calculate the rate."""
    total_classes = get_valid_number(
        "Enter total number of classes held: ", minimum=1, number_type=int
    )
    while True:
        attended_classes = get_valid_number(
            "Enter number of classes attended: ", minimum=0, number_type=int
        )
        if attended_classes > total_classes:
            print("Classes attended cannot exceed total classes held.")
            continue
        break

    attendance_rate = (attended_classes / total_classes) * 100
    return attendance_rate


def print_report(name, roll_number, subjects, average, grade, attendance_rate):
    """Print a clean, formatted report card."""
    min_attendance_required = 75
    is_eligible = attendance_rate >= min_attendance_required

    print("\n" + "=" * 45)
    print("           STUDENT REPORT CARD")
    print("=" * 45)
    print(f"Name        : {name}")
    print(f"Roll Number : {roll_number}")
    print("-" * 45)
    print("Subject Marks:")
    for subject, marks in subjects.items():
        print(f"  - {subject:<20}: {marks:.1f}")
    print("-" * 45)
    print(f"Average Marks     : {average:.2f}%")
    print(f"Final Grade       : {grade}")
    print(f"Attendance Rate   : {attendance_rate:.2f}%")
    print(f"Exam Eligibility  : {'Eligible' if is_eligible else 'Not Eligible (attendance below 75%)'}")
    print("=" * 45)


def main():
    print("=" * 45)
    print("   STUDENT GRADE & ATTENDANCE TRACKER")
    print("=" * 45)

    name, roll_number = collect_student_info()
    subjects = collect_subject_marks()
    average = calculate_average(subjects)
    grade = assign_grade(average)
    attendance_rate = collect_attendance()

    print_report(name, roll_number, subjects, average, grade, attendance_rate)


if __name__ == "__main__":
    main()
