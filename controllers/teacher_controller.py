from random import choice

from classes.teacher import Teacher

TEACHERS = [
    Teacher("Edit", ("Maths", "FurtherMaths"), 205),
    Teacher("Lewis", ("Maths", "FurtherMaths"), 208),
    Teacher("David", ("ComputerScience", "IT"), 308),
]


def teacher_selector(subject: str) -> Teacher | None:
    """Selects a suitable teacher for a lesson

    Args:
        subject (str): The subject of the lesson

    Returns:
        Teacher | None: Returns a teacher or None
    """

    # Searches for available teachers that teach the subject
    available_teachers = [
        teacher
        for teacher in TEACHERS
        if teacher.is_available() and subject in teacher.get_subjects()
    ]

    # Returns a random available teacher or None
    return choice(available_teachers) if len(available_teachers) != 0 else None
