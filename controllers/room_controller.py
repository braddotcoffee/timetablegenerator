from teacher import Teacher

ROOMS = {
    "Maths": [201, 205, 206, 207, 208],
    "FurtherMaths": [201, 205, 206, 207, 208],
    "ComputerScience": [305, 306, 307, 308],
}


def room_selector(subject: str, teacher: Teacher) -> int | None:
    """Selects a suitable room for a lesson

    Args:
        subject (str): The subject of the lesson
        teacher (Teacher): The teacher teaching the lesson

    Returns:
        int | None: Returns a room number or None
    """

    # Add more checks to select the room such as distance between rooms, is the room in use etc

    if teacher.get_pref_room():
        return (
            teacher.get_pref_room()
            if teacher.get_pref_room() in ROOMS[subject]
            else None
        )
