from copy import deepcopy
import pandas as pd
from typing import List, Dict

from classes.timetable import Timetable

DEFAULT_DATA = {
    "Mon": {
        "P1": {"Class": "", "Room": 0},
        "P2": {"Class": "", "Room": 0},
        "P3": {"Class": "", "Room": 0},
        "P4": {"Class": "", "Room": 0},
        "P5": {"Class": "", "Room": 0},
        "P6": {"Class": "", "Room": 0},
    },
    "Tue": {
        "P1": {"Class": "", "Room": 0},
        "P2": {"Class": "", "Room": 0},
        "P3": {"Class": "", "Room": 0},
        "P4": {"Class": "", "Room": 0},
        "P5": {"Class": "", "Room": 0},
        "P6": {"Class": "", "Room": 0},
    },
    "Wed": {
        "P1": {"Class": "", "Room": 0},
        "P2": {"Class": "", "Room": 0},
        "P3": {"Class": "", "Room": 0},
        "P4": {"Class": "", "Room": 0},
        "P5": {"Class": "", "Room": 0},
        "P6": {"Class": "", "Room": 0},
    },
    "Thu": {
        "P1": {"Class": "", "Room": 0},
        "P2": {"Class": "", "Room": 0},
        "P3": {"Class": "", "Room": 0},
        "P4": {"Class": "", "Room": 0},
        "P5": {"Class": "", "Room": 0},
        "P6": {"Class": "", "Room": 0},
    },
}


class Teacher(Timetable):
    def __init__(
        self,
        name: str,
        subjects: List[str],
        room: int,
        timetable: Dict[str, Dict[str, Dict[str, str | int]]] = deepcopy(DEFAULT_DATA),
    ) -> None:
        super().__init__(timetable)
        self.name = name
        self.subjects = subjects
        self.pref_room = room
        self.timetable = timetable

    def __repr__(self) -> str:
        # ! WORKS DO NOT TOUCH
        rows = []
        for day, periods in self.timetable.items():
            for period, data in periods.items():
                rows.extend(
                    [
                        (day, f"{period} Class", data["Class"]),
                        (day, f"{period} Room", data["Room"]),
                    ]
                )
        df = pd.DataFrame(rows, columns=["Day", "Period", "Data"])
        df = df.pivot(index="Period", columns="Day", values="Data")
        df.reset_index(drop=True)

        return f"Teacher: name={self.name}, subjects={self.subjects}, pref_room={self.pref_room} timetable=\n{df.to_string()}"

    # Getters

    def get_name(self):
        return self.name

    def get_subjects(self):
        return self.subjects

    def get_pref_room(self):
        return self.pref_room

    # Setters

    def set_available(self, value):
        self.available = value
