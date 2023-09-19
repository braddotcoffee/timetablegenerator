import json

from classes.room import Room
from classes.teacher import Teacher


with open("data/teachers.json", "r") as read_file:
    teacher_data = json.load(read_file)

with open("data/rooms.json", "r") as read_file:
    room_data = json.load(read_file)

TEACHERS = [
    Teacher(v["Name"], v["Subjects"], v["PreferredRoom"]) for v in teacher_data.values()
]

ROOMS = [
    Room(v["RoomNumber"], v["Available"], v["Subjects"], v["Capacity"])
    for v in room_data.values()
]

CLASS_SETS = ["Ma12B", "Ma12A", "CS12A", "Cs12B", "FM12A"]
