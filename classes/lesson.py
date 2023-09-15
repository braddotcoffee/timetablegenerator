from classes.student import Student
from classes.teacher import Teacher
from typing import List


class Lesson:
    def __init__(
        self,
        teacher: Teacher,
        students: List[Student],
        room: dict[int, bool, List[str]],
        subject: str,
        period: int,
    ) -> None:
        self.teacher = teacher
        self.students = students
        self.room = room
        self.subject = subject
        self.period = period

        # All the stuff that happens when a lesson is created. E.g. teacher, room, and students becomes unavailable for the period
        self.teacher.available = False
        self.room["Available"] = False

    def __repr__(self) -> str:
        return (
            f"{self.subject} Lesson:\n"
            f"Teacher: {self.teacher.get_name()}\n"
            f"Room: {self.room['RoomNumber']}\n"
            f"Student one: {self.students[0].get_name()}\n"
            f"Student two: {self.students[1].get_name()}\n"
            f"Student three: {self.students[2].get_name()}\n"
            f"Student four: {self.students[3].get_name()}\n"
        )
