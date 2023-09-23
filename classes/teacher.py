from typing import List


DEFAULT_DATA = {
    "P1 ClassSet": ["", "", "", ""],
    "P1 Room": [0, 0, 0, 0],
    "P2 ClassSet": ["", "", "", ""],
    "P2 Room": [0, 0, 0, 0],
    "P3 ClassSet": ["", "", "", ""],
    "P3 Room": [0, 0, 0, 0],
    "P4 ClassSet": ["", "", "", ""],
    "P4 Room": [0, 0, 0, 0],
    "P5 ClassSet": ["", "", "", ""],
    "P5 Room": [0, 0, 0, 0],
    "P6 ClassSet": ["", "", "", ""],
    "P6 Room": [0, 0, 0, 0],
}


class Teacher:
    def __init__(
        self,
        name: str,
        subjects: List[str],
        room: int,
        available: bool = True,
    ) -> None:
        self.name = name
        self.subjects = subjects
        self.pref_room = room
        self.available = available

    def __repr__(self) -> str:
        return f"Teacher: name={self.name}, subjects={self.subjects}, pref_room={self.pref_room}, available={self.available}"

    # Getters

    def get_name(self):
        return self.name

    def get_subjects(self):
        return self.subjects

    def get_pref_room(self):
        return self.pref_room

    def is_available(self):
        return self.available

    # Setters

    def set_available(self, value):
        self.available = value
