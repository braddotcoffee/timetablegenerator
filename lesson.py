from student import Student
from teacher import Teacher
from typing import List


class Lesson:
    def __init__(
        self, teacher: Teacher, students: List[Student], room: int, subject: str
    ) -> None:
        self.teacher = teacher
        self.students = students
        self.room = room
        self.subject = subject

    def __repr__(self) -> str:
        return f"Lesson: subject={self.subject}, teacher={self.teacher}, room={self.room}, students={self.students}"
