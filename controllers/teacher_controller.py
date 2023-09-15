from teacher import Teacher


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

    for teacher in TEACHERS:
        if subject not in teacher.get_subjects():
            return None
        if not teacher.is_available():
            return None

        return teacher
