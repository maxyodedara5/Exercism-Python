PLANTS = {
    "V" : "Violets",
    "R" : "Radishes",
    "G" : "Grass",
    "C" : "Clover"
    }


class Garden:
    """Class for giving plants"""
    def __init__(self, diagram,
                 students=[
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        """Gives plants for the students"""
        student_roll = self.students.index(student)
        student_plants = []
        for plant in self.diagram:
            student_plants.append(plant[2 * student_roll : 2 * student_roll + 2])

        student_plants = "".join(student_plants)
        ans_plants = []
        for plant in student_plants:
            ans_plants.append(PLANTS[plant])

        return ans_plants
