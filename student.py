from typing import Tuple


class Student:
    def __init__(self, name: str, subjects: Tuple[str, str, str]) -> None:
        self.name = name
        self.subjects = subjects

    def __repr__(self) -> str:
        return f"Student: name={self.name}, subjects={self.subjects}"

    def get_subjects(self):
        return self.subjects
