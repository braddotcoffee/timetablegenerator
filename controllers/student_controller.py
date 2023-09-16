from typing import List

from classes.student import Student
from controllers.data_controller import STUDENTS

CLASS_SIZE = 20


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
        # Limits the class size to the specified amount in the constant
        if len(classStudents) == CLASS_SIZE:
            return classStudents

        # Checks if the student hasn't already got a lesson, and does the subject of the lesson
        if subject in student.get_subjects() and student.is_available():
            # Sets the students availability
            student.set_available(False)
            # Adds the student to the class
            classStudents.append(student)

    # Returns the list of students if there is at least one student selected otherwise it returns None
    return classStudents if classStudents else None
