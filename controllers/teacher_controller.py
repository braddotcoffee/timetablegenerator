from classes.teacher import Teacher
from data.teachers import TEACHERS


def teacher_selector(subject: str) -> Teacher | None:
    """Selects a suitable teacher for a lesson

    Args:
        subject (str): The subject of the lesson

    Returns:
        Teacher | None: Returns a teacher or None
    """

    # Searches for available teachers
    available_teachers = [teacher for teacher in TEACHERS if teacher.is_available()]

    # Searches the available teachers to check:
    # 1. If the teacher teaches the subject needed
    for teacher in available_teachers:
        if subject not in teacher.get_subjects():
            continue

        return teacher

    # Just prints out this if there aren't any available teachers. Idk what happens after this
    print("No teachers available")
    return None
