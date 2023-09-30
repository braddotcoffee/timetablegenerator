from typing import Dict


class Timetable:
    def __init__(
        self,
    ) -> None:
        self.timetable = Timetable._default_timetable()

    @staticmethod
    def _default_timetable():
        return {
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

    def get_class_set(self, day, period):
        return self.timetable[day][period]["Class"]

    def get_room(self, day, period):
        return self.timetable[day][period]["Room"]

    def set_class_set(self, classSet: str, day: int, period: int):
        try:
            self.timetable[day][period]["Class"] = classSet
        except IndexError:
            # self.timetable[day][period]["Class"] = classSet
            print("IndexError: list assignment index out of range")
            print(f"Period: {period}, Day: {day}")

    def set_room(self, room: int, day: int, period: int):
        try:
            self.timetable[day][period]["Room"] = room
        except IndexError:
            # self.timetable[day][period]["Room"] = room
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
