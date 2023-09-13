from lesson import Lesson

from controllers.room_controller import room_selector
from controllers.student_controller import student_selector
from controllers.teacher_controller import teacher_selector


mathsLessonOneTeacher = teacher_selector("Maths")
mathsLessonOneStudents = student_selector("Maths")
mathsLessonOneRoom = room_selector("Maths", mathsLessonOneTeacher)

mathsLessonOne = Lesson(
    mathsLessonOneTeacher, mathsLessonOneStudents, mathsLessonOneRoom, "Maths"
)

print(mathsLessonOne)


# TODO: Make the list of teachers in teacher_controller.py only a list of available teachers
# TODO:
