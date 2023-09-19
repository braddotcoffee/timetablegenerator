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
    "P1 Subject": ["a", "b", "c", "d", "e"],
    "P1 ClassSet": ["a", "b", "c", "d", "e"],
    "P1 Room": [1, 2, 3, 4, 5],
    "P2 Subject": ["a", "b", "c", "d", "e"],
    "P2 ClassSet": ["a", "b", "c", "d", "e"],
    "P2 Room": [1, 2, 3, 4, 5],
    "P3 Subject": ["a", "b", "c", "d", "e"],
    "P3 ClassSet": ["a", "b", "c", "d", "e"],
    "P3 Room": [1, 2, 3, 4, 5],
    "P4 Subject": ["a", "b", "c", "d", "e"],
    "P4 ClassSet": ["a", "b", "c", "d", "e"],
    "P4 Room": [1, 2, 3, 4, 5],
}

default_data = {
    "P1 Subject": ["", "", "", "", ""],
    "P1 ClassSet": ["", "", "", "", ""],
    "P1 Room": [0, 0, 0, 0, 0],
    "P2 Subject": ["", "", "", "", ""],
    "P2 ClassSet": ["", "", "", "", ""],
    "P2 Room": [0, 0, 0, 0, 0],
    "P3 Subject": ["", "", "", "", ""],
    "P3 ClassSet": ["", "", "", "", ""],
    "P3 Room": [0, 0, 0, 0, 0],
    "P4 Subject": ["", "", "", "", ""],
    "P4 ClassSet": ["", "", "", "", ""],
    "P4 Room": [0, 0, 0, 0, 0],
}

DAYS_TO_TIMETABLE_INDEX = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
}


class Timetable:
    def __init__(self, data: dict[str, List[str | int]] = default_data) -> None:
        self.timetable = pd.DataFrame.from_dict(
            data=data,
            orient="index",
            columns=["Mon", "Tue", "Wed", "Thu"],
        )

    def __repr__(self) -> str:
        return f"Timetable:\n{self.timetable}"

    def set_subject(self, subject, day):
        self.timetable.loc[f"P{DAYS_TO_TIMETABLE_INDEX[day]} Subject", [day]] = subject

    def set_class_set(self, class_set, day):
        self.timetable.loc[
            f"P{DAYS_TO_TIMETABLE_INDEX[day]} ClassSet", [day]
        ] = class_set

    def set_room(self, room: Room, day):
        self.timetable.loc[
            f"P{DAYS_TO_TIMETABLE_INDEX[day]} Room", [day]
        ] = room.room_number
