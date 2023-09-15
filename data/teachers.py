import json

from classes.teacher import Teacher


with open("data/teachers.json", "r") as read_file:
    data = json.load(read_file)

TEACHERS = [
    Teacher(v["Name"], v["Subjects"], v["PreferredRoom"]) for v in data.values()
]
