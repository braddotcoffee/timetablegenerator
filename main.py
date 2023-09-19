from classes.lesson import Lesson

from controllers.room_controller import room_selector
from controllers.teacher_controller import teacher_selector


mathsLessonOneTeacher = teacher_selector("Maths")
mathsLessonOneRoom = room_selector("Maths", mathsLessonOneTeacher)

mathsLessonOne = Lesson(
    mathsLessonOneTeacher,
    "Ma12B",
    mathsLessonOneRoom,
    "Maths",
    3,
    "Tue",
)

computerScienceTeacher = teacher_selector("ComputerScience")

print(mathsLessonOne)
print(mathsLessonOneTeacher.timetable.print_timetable())
print(mathsLessonOneTeacher.is_available())

# TODO: DO THE CREATE GENOME FUNCTION IN genetic_algorithm.py

# // TODO: Make a timetable for one of the teachers using their current classes

# // TODO: Make a teacher timetables containing subject, period, class, and room for each lesson assuming KS4 don't exist
# // TODO: When doing the task above, make sure that lessons are spread out, and students don't have one lesson P1, one lesson P6
# // TODO: Format the lessons in a nicer way than the console
# // TODO: Add inclusion of KS4 students

# ? Data required for the program:
# * Teachers: The subjects they teach, and their preferred room
# * Rooms: Capacity of each room, and what subjects can be taught in them
# * Students: What subjects students take
