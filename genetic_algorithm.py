from enum import Enum
from random import choice
from typing import Dict, List

from controllers.data_controller import CLASS_SETS, ROOMS, TEACHERS
from controllers.room_controller import room_selector
from classes.timetable import Timetable

# * Notes:
# * The genes will be the lessons
# * A chromosome is a complete set of genes
# * Genes will be generated by generating all random "chromosomes" (factors) of a lesson
# * A genome is the same as a lesson


class Subjects(Enum):
    MATHS = "Maths"
    FURTHER_MATHS = "FurtherMaths"
    COMPUTER_SCIENCE = "ComputerScience"
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    PHYSICS = "Physics"
    IT = "IT"


def create_genome_check_timetable(lessons: List[List[str]]) -> bool:
    for period in lessons:
        for day in period:
            if day != "":
                return True
    return False


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key, value)


class Individual:
    """This is a whole working timetable of all the teachers"""

    def __init__(self) -> None:
        self.fitness = self.calc_fitness()

    def generate_mutation(self):
        mutation_choice = choice(["ClassSet", "Room"])
        mutation_day = choice(["Mon", "Tue", "Wed", "Thu"])
        mutation_period = choice([1, 2, 3, 4, 5, 6])
        if mutation_choice == "ClassSet":
            random_set = None
            while (
                self.timetable_genome.get_class_set(mutation_day, mutation_period)
                != random_set
            ):
                random_set = choice(CLASS_SETS["SetName"])
                self.timetable_genome.set_class_set(
                    random_set, mutation_day, mutation_period
                )
        else:
            random_room = None
            while (
                self.timetable_genome.get_room(mutation_day, mutation_period)
                != random_room
            ):
                random_room = choice(ROOMS["RoomName"])
                self.timetable_genome.set_room(
                    random_room, mutation_day, mutation_period
                )

    def create_genome(self) -> Dict[str, Timetable]:
        """
        Generates random timetables for the whole school.
        Every class needs 5 lessons a week
        """

        list_of_teachers = [teacher for teacher in TEACHERS]

        list_of_available_class_sets = [
            class_set for class_set in CLASS_SETS if class_set["LessonsInWeek"] != 5
        ]

        teachers_generated_counter = 0

        while list_of_available_class_sets:
            # Loops through all the teachers, creating timetables for each one and appends them to the list_of_teacher_timetable
            for teacher in list_of_teachers:
                # Removes fully-classed classes from the list of available classes
                for class_set_x in list_of_available_class_sets:
                    if class_set_x["LessonsInWeek"] == 5:
                        list_of_available_class_sets.remove(class_set_x)

                try:
                    class_set = choice(list_of_available_class_sets)
                except:
                    print("No more classes")
                    break

                # Checks if the teacher teaches that subject
                if class_set["Subject"] in teacher.get_subjects():
                    # Sets the room for the class
                    room = room_selector(class_set["Subject"], teacher)

                    # Gets the timetable of this teacher
                    teacher_timetable = teacher.timetable

                    # Gets the available lessons of this teacher
                    available_lessons = teacher_timetable.get_available_lessons()

                    # If the teacher has at least one available lesson (this is ok because it
                    # means that every other teacher must have roughly the same amount of lessons)
                    if len(available_lessons) != 0:
                        # Choose a random lesson slot (period and day)
                        random_lesson = choice(available_lessons)
                        day = random_lesson[0]
                        period = random_lesson[1]

                        # Sets the ClassSet on the teacher's timetable
                        teacher_timetable.set_class_set(
                            class_set["SetName"], day, period
                        )

                        # Sets the room on the teacher's timetable
                        teacher_timetable.set_room(room.get_room_number(), period, day)

                        class_set["LessonsInWeek"] += 1
                        break
                    else:
                        print("Teacher has no more available lessons")
                        for teacher in list_of_teachers:
                            print(teacher)
                        return list_of_teachers

                teachers_generated_counter += 1
                print(teachers_generated_counter)

        return list_of_teachers

    def crossover(self, otherTimetable: Timetable) -> List[Timetable]:
        pass

    def calc_fitness(self):
        pass


class GeneticAlgorithm:
    def __init__(self, timetable: Dict[str, List[str | int]]) -> None:
        self.timetable = timetable


individual = Individual()
individual.create_genome()
