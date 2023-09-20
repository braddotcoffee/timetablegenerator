from typing import List
import pandas as pd

from classes.room import Room

import sys
import os

from classes.teacher import Teacher

#! DO NOT TOUCH THE WEIRD SYS PATH IT WORKS SO KEEP IT
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())


# * data should be in the format displayed below:

test_data = {
    "P1 ClassSet": ["a", "b", "c", "d"],
    "P1 Room": [1, 2, 3, 4],
    "P2 ClassSet": ["a", "b", "c", "d"],
    "P2 Room": [1, 2, 3, 4],
    "P3 ClassSet": ["a", "b", "c", "d"],
    "P3 Room": [1, 2, 3, 4],
    "P4 ClassSet": ["a", "b", "c", "d"],
    "P4 Room": [1, 2, 3, 4],
    "P5 ClassSet": ["a", "b", "c", "d"],
    "P5 Room": [1, 2, 3, 4],
    "P6 ClassSet": ["a", "b", "c", "d"],
    "P6 Room": [1, 2, 3, 4],
}

default_data = {
    "P1 ClassSet": ["", "", "", ""],
    "P1 Room": [0, 0, 0, 0],
    "P2 ClassSet": ["", "", "", ""],
    "P2 Room": [0, 0, 0, 0],
    "P3 ClassSet": ["", "", "", ""],
    "P3 Room": [0, 0, 0, 0],
    "P4 ClassSet": ["", "", "", ""],
    "P4 Room": [0, 0, 0, 0],
    "P5 ClassSet": ["", "", "", ""],
    "P5 Room": [0, 0, 0, 0],
    "P6 ClassSet": ["", "", "", ""],
    "P6 Room": [0, 0, 0, 0],
}

DAYS_TO_TIMETABLE_INDEX = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
}


class Timetable:
    def __init__(
        self, teacher: Teacher, timetable: dict[str, List[str | int]] = default_data
    ) -> None:
        self.teacher = teacher
        self.timetable = timetable

    def get_class_set(self, day, period):
        return self.timetable[f"P{period} ClassSet"][DAYS_TO_TIMETABLE_INDEX[day]]

    def get_room(self, day, period):
        return self.timetable[f"P{period} Room"][DAYS_TO_TIMETABLE_INDEX[day]]

    def set_class_set(self, classSet, day, period):
        self.timetable[f"P{period} ClassSet"][DAYS_TO_TIMETABLE_INDEX[day]] = classSet

    def set_room(self, period: int, room: Room, day):
        self.timetable[f"P{period} Room"][
            DAYS_TO_TIMETABLE_INDEX[day]
        ] = room.room_number

    def print_timetable(self):
        timetable = pd.DataFrame.from_dict(
            data=self.timetable, orient="index", columns=["Mon", "Tue", "Wed", "Thur"]
        )
        print(timetable.to_string())

    def get_available_lessons(self):
        available_lessons = []
        lessons = [
            [i for i in self.timetable[x] if isinstance(i, str)]
            for x in self.timetable.keys()
        ]
        for lesson in lessons:
            if len(lesson) == 0:
                lessons.remove(lesson)

        for i, x in enumerate(lessons):
            if "" in x:
                available_lessons.append((i, x.index("")))

        return available_lessons
