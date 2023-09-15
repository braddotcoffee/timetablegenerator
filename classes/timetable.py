from typing import List
from pandas import DataFrame as df

from classes.lesson import Lesson
from classes.teacher import Teacher


class Timetable:
    def __init__(self, teacher: Teacher, lessons: dict[str, List[Lesson]]) -> None:
        self.teacher = teacher
        self.timetable = df.from_dict(
            data=lessons,
            orient="index",
            columns=["Mon", "Tue", "Wed", "Thu", "Fri"],
        )
