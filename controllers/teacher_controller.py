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

    # Add more checks to select the teacher such as availability etc

    for teacher in TEACHERS:
        if subject in teacher.get_subjects():
            return teacher

    return None
