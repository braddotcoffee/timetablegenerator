from typing import List
import pandas as pd

from classes.room import Room

import sys
import os

from classes.teacher import DEFAULT_DATA, Teacher

#! DO NOT TOUCH THE WEIRD SYS PATH IT WORKS SO KEEP IT
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())


# * data should be in the format displayed below:


DAYS_TO_TIMETABLE_INDEX = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
}

TIMETABLE_INDEX_TO_DAYS = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
}


class Timetable:
    def __init__(
        self, teacher: Teacher, timetable: dict[str, List[str | int]] = DEFAULT_DATA
    ) -> None:
        self.teacher = teacher
        self.timetable = timetable

    def __repr__(self):
        timetable = pd.DataFrame.from_dict(
            data=self.timetable, orient="index", columns=["Mon", "Tue", "Wed", "Thur"]
        )
        return timetable.to_string()

    def get_class_set(self, day, period):
        return self.timetable[f"P{period} ClassSet"][DAYS_TO_TIMETABLE_INDEX[day]]

    def get_room(self, day, period):
        return self.timetable[f"P{period} Room"][DAYS_TO_TIMETABLE_INDEX[day]]

    def set_class_set(self, classSet: str, day: int, period: int):
        try:
            self.timetable[f"P{period} ClassSet"][day] = classSet
        except:
            self.timetable[f"P{period} ClassSet"][day - 1] = classSet
            print("IndexError: list assignment index out of range")
            print(f"Period: {period}, Day: {day}")

    def set_room(self, room: int, period: int, day: int):
        try:
            self.timetable[f"P{period} Room"][day] = room
        except:
            self.timetable[f"P{period} Room"][day - 1] = room
            print("IndexError: list assignment index out of range")
            print(f"Period: {period}, Day: {day}")

    def get_available_lessons(self):
        # ! WORKS FINE DO NOT TOUCH
        available_lessons = []
        lessons = [
            [i for i in self.timetable[x] if isinstance(i, str)]
            for x in self.timetable.keys()
        ]
        for lesson in lessons:
            if len(lesson) == 0:
                lessons.remove(lesson)

        counter = 1
        for period in lessons:
            for i in range(len(period)):
                if period[i] == "":
                    available_lessons.append((counter, i + 1))
                    print(counter, i)
            counter += 1

        return available_lessons
