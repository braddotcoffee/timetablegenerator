from classes.teacher import Teacher
from data.rooms import ROOMS


def room_selector(subject: str, teacher: Teacher) -> int | None:
    """Selects a suitable room for a lesson

    Args:
        subject (str): The subject of the lesson
        teacher (Teacher): The teacher teaching the lesson

    Returns:
        int | None: Returns a room number or None
    """

    # TODO: Add more checks to select the room such as distance between rooms, is the room in use etc

    # Searches each room in to check if it is the teachers preferred room, it is available, and if the subject can be taught in the room
    for room in ROOMS[subject]:
        if (
            teacher.get_pref_room() == room["RoomNumber"]
            and room["Available"]
            and subject in room["Subjects"]
        ):
            return room

    # Searches each room to check if it is available and if the subject can be taught in the room
    for room in ROOMS[subject]:
        if room["Available"] and subject in room["Subjects"]:
            return room

    # Just prints out this if there aren't any available rooms. Idk what happens after this
    print("No rooms available")
    return None
