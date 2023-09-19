from typing import List
import pandas as pd

from classes.room import Room

import sys
import os

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
}

DAYS_TO_TIMETABLE_INDEX = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
}


class Timetable:
    def __init__(self, timetable: dict[str, List[str | int]] = default_data) -> None:
        self.timetable = timetable

    def get_class_set(self, day, period):
        return self.timetable[f"{period} ClassSet"][DAYS_TO_TIMETABLE_INDEX[day] - 1]

    def get_room(self, day, period):
        return self.timetable[f"{period} Room"][DAYS_TO_TIMETABLE_INDEX[day] - 1]

    def set_class_set(self, classSet, day, period):
        self.timetable[f"P{period} ClassSet"][
            DAYS_TO_TIMETABLE_INDEX[day] - 1
        ] = classSet

    def set_room(self, room: Room, day):
        self.timetable[f"P{DAYS_TO_TIMETABLE_INDEX[day]} Room"][
            DAYS_TO_TIMETABLE_INDEX[day] - 1
        ] = room.room_number

    def print_timetable(self):
        timetable = pd.DataFrame.from_dict(
            data=self.timetable, orient="index", columns=["Mon", "Tue", "Wed", "Thur"]
        )
        print(timetable.to_string())
