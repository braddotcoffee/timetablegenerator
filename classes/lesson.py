from classes.room import Room
from classes.teacher import Teacher


class Lesson:
    def __init__(
        self,
        teacher: Teacher,
        class_set: str,
        room: Room,
        subject: str,
        period: int,
        day: str,
    ) -> None:
        self.teacher = teacher
        self.class_set = class_set
        self.room = room
        self.subject = subject
        self.period = period
        self.day = day

        # All the stuff that happens when a lesson is created. E.g. teacher, room, and students becomes unavailable for the period
        self.teacher.available = False
        self.room.available = False

        # Sets the timeslots on the teacher's timetable to those of this lesson
        self.teacher.timetable.set_class_set(self.class_set, self.day, self.period)
        self.teacher.timetable.set_room(self.room, self.day)

    def __repr__(self) -> str:
        return (
            f"{self.subject} Lesson:\n"
            f"Teacher: {self.teacher.get_name()}\n"
            f"Room: {self.room.room_number}\n"
        )

    def get_teacher(self):
        return self.teacher

    def get_room(self):
        return self.room

    def get_subject(self):
        return self.subject
