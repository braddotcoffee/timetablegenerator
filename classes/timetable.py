from typing import List
import pandas as pd

import sys
import os

#! DO NOT TOUCH THE WEIRD SYS PATH IT WORKS SO KEEP IT
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())


from teacher import Teacher
from data.teachers import TEACHERS

# * data should be in the format displayed below:

test_data = {
    "P1 Subject": ["a", "b", "c", "d", "e"],
    "P1 Class": ["a", "b", "c", "d", "e"],
    "P1 Room": [1, 2, 3, 4, 5],
    "P2 Subject": ["a", "b", "c", "d", "e"],
    "P2 Class": ["a", "b", "c", "d", "e"],
    "P2 Room": [1, 2, 3, 4, 5],
    "P3 Subject": ["a", "b", "c", "d", "e"],
    "P3 Class": ["a", "b", "c", "d", "e"],
    "P3 Room": [1, 2, 3, 4, 5],
    "P4 Subject": ["a", "b", "c", "d", "e"],
    "P4 Class": ["a", "b", "c", "d", "e"],
    "P4 Room": [1, 2, 3, 4, 5],
    "P5 Subject": ["a", "b", "c", "d", "e"],
    "P5 Class": ["a", "b", "c", "d", "e"],
    "P5 Room": [1, 2, 3, 4, 5],
}


class Timetable:
    def __init__(self, teacher: Teacher, data: dict[str, List[str | int]]) -> None:
        self.teacher = teacher
        self.timetable = pd.DataFrame.from_dict(
            data=data,
            orient="index",
            columns=["Mon", "Tue", "Wed", "Thu", "Fri"],
        )


timetable = Timetable(TEACHERS[0], test_data)

print(timetable.timetable.to_string())
