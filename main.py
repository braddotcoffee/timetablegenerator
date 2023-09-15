from classes.lesson import Lesson

from controllers.room_controller import room_selector
from controllers.student_controller import student_selector
from controllers.teacher_controller import teacher_selector


mathsLessonOneTeacher = teacher_selector("Maths")
mathsLessonOneStudents = student_selector("Maths")
mathsLessonOneRoom = room_selector("Maths", mathsLessonOneTeacher)

mathsLessonOne = Lesson(
    mathsLessonOneTeacher, mathsLessonOneStudents, mathsLessonOneRoom, "Maths", 1
)

print(mathsLessonOne)

# TODO: Make a timetable for one of the teachers using their current classes

# TODO: Make a teacher timetables containing subject, period, class, and room for each lesson assuming KS4 don't exist
# TODO: When doing the task above, make sure that lessons are spread out, and students don't have one lesson P1, one lesson P6
# TODO: Format the lessons in a nicer way than the console
# TODO: Add inclusion of KS4 students
