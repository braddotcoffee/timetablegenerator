from typing import Tuple


class Teacher:
    def __init__(self, name: str, subjects: Tuple[str, str], room) -> None:
        self.name = name
        self.subjects = subjects
        self.pref_room = room

    def __repr__(self) -> str:
        return f"Teacher: name={self.name}, subjects={self.subjects}, pref_room={self.pref_room}"
