import pandas as pd
from typing import List

from classes.timetable import Timetable


class Teacher:
    def __init__(
        self,
        name: str,
        subjects: List[str],
        room: int,
    ) -> None:
        self.name = name
        self.subjects = subjects
        self.pref_room = room
        self.timetable = Timetable()

    def __repr__(self) -> str:
        # ! WORKS DO NOT TOUCH
        rows = []
        for day, periods in self.timetable.timetable.items():
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
