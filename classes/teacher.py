from typing import List

from classes.timetable import Timetable


class Teacher:
    def __init__(
        self,
        name: str,
        subjects: List[str],
        room: int,
        timetable: Timetable = Timetable(),
    ) -> None:
        self.name = name
        self.subjects = subjects
        self.pref_room = room
        self.timetable = timetable

    def __repr__(self) -> str:
        return f"Teacher: name={self.name}, subjects={self.subjects}, pref_room={self.pref_room} timetable=\n{self.timetable}"

    # Getters

    def get_name(self):
        return self.name

    def get_subjects(self):
        return self.subjects

    def get_pref_room(self):
        return self.pref_room

    # Setters

    def set_available(self, value):
        self.available = value
