from teacher import Teacher
from rooms import ROOMS


def room_selector(subject: str, teacher: Teacher) -> int | None:
    """Selects a suitable room for a lesson

    Args:
        subject (str): The subject of the lesson
        teacher (Teacher): The teacher teaching the lesson

    Returns:
        int | None: Returns a room number or None
    """

    # Add more checks to select the room such as distance between rooms, is the room in use etc

    for room in ROOMS[subject]:
        if teacher.get_pref_room() == room["RoomNumber"] and room["Available"]:
            return room

    return None
