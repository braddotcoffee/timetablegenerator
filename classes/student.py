from typing import List


class Student:
    def __init__(self, name: str, subjects: List[str], available: bool = True) -> None:
        self.name = name
        self.subjects = subjects
        self.available = available

    def __repr__(self) -> str:
        return f"Student: name={self.name}, subjects={self.subjects}, available={'Yes' if self.available else 'No'}"

    # Getters
    def get_name(self):
        return self.name

    def get_subjects(self):
        return self.subjects

    def is_available(self):
        return self.available

    # Setters
    def set_available(self, value):
        self.available = value
