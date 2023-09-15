from typing import Tuple


class Teacher:
    def __init__(
        self, name: str, subjects: Tuple[str, str], room: int, available: bool
    ) -> None:
        self.name = name
        self.subjects = subjects
        self.pref_room = room
        self.available = available

    def __repr__(self) -> str:
        return f"Teacher: name={self.name}, subjects={self.subjects}, pref_room={self.pref_room}, available={self.available}"

    # Getters
    def get_subjects(self):
        return self.subjects

    def get_pref_room(self):
        return self.pref_room

    def is_available(self):
        return self.available

    # Setters

    def set_available(self, value):
        self.available = value
