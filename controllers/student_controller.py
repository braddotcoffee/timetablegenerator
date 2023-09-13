from typing import List

from student import Student

STUDENTS = [
    Student("studentOne", ("Maths", "FurtherMaths", "ComputerScience")),
    Student("studentTwo", ("Maths", "FurtherMaths", "ComputerScience")),
    Student("studentThree", ("Maths", "FurtherMaths", "ComputerScience")),
    Student("studentFour", ("Maths", "FurtherMaths", "ComputerScience")),
]


def student_selector(subject: str) -> List[Student] | None:
    """Selects a list of students for a lesson

    Args:
        subject (str): The subject of the lesson

    Returns:
        List[Student] | None: Returns a list of students or None
    """

    # Add more checks to select students such as student ability etc

    classStudents = []

    for student in STUDENTS:
        if len(classStudents) == 20:
            return classStudents

        if subject in student.get_subjects():
            classStudents.append(student)

    return classStudents if classStudents else None
