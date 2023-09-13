from typing import List
from pandas import DataFrame as df
from lesson import Lesson


class StudentTimetable:
    def __init__(self, studentName: str, lessons: dict[str, List[Lesson]]) -> None:
        self.name = studentName
        self.timetable = df.from_dict(
            data=lessons,
            orient="index",
            columns=["Mon", "Tue", "Wed", "Thu", "Fri"],
        )
