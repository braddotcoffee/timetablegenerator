from student import Student
from teacher import Teacher
from typing import List


class Lesson:
    def __init__(
        self,
        teacher: Teacher,
        students: List[Student],
        room: int,
        subject: str,
        period: int,
    ) -> None:
        self.teacher = teacher
        self.students = students
        self.room = room
        self.subject = subject
        self.period = period

        self.teacher.available = False

    def __repr__(self) -> str:
        return f"Lesson: subject={self.subject}, teacher={self.teacher}, room={self.room}, students={self.students}"

    def create_lesson(self):
        # All the stuff that happens when a lesson is created. E.g. teacher, room, and students becomes unavailable for the period

        self.teacher.set_available(False)
