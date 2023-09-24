from typing import Dict


class Timetable:
    def __init__(
        self,
        timetable: Dict[str, Dict[str, Dict[str, str | int]]],
    ) -> None:
        self.timetable = timetable

    def get_class_set(self, day, period):
        return self.timetable[day][period]["Class"]

    def get_room(self, day, period):
        return self.timetable[day][period]["Room"]

    def set_class_set(self, classSet: str, day: int, period: int):
        try:
            self.timetable[day][period]["Class"] = classSet
        except:
            self.timetable[day][period]["Class"] = classSet
            print("IndexError: list assignment index out of range")
            print(f"Period: {period}, Day: {day}")

    def set_room(self, room: int, day: int, period: int):
        try:
            self.timetable[day][period]["Room"] = room
        except:
            self.timetable[day][period]["Room"] = room
            print("IndexError: list assignment index out of range")
            print(f"Period: {period}, Day: {day}")

    def get_available_lessons(self):
        # ! WORKS FINE DO NOT TOUCH maybe?
        available_lessons = []

        for day_k, day_v in self.timetable.items():
            for period_k, period_v in day_v.items():
                for class_k, class_v in period_v.items():
                    if type(class_v) == str and class_v == "":
                        available_lessons.append([day_k, period_k, class_k])

        return available_lessons
