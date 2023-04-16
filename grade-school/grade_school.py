"""Class School logic for adding students"""

class School:
    """School logic for adding students"""
    def __init__(self):
        self.students = {}
        self.added_history = []

    def add_student(self, name, grade):
        """Adds student to the roster"""
        already_present = False
        for grades in self.students: # pylint: disable=C0206
            if name in self.students[grades]:
                already_present = True

        if already_present:
            self.added_history.append(False)
        else:
            self.added_history.append(True)
            if grade not in self.students:
                self.students[grade] = []
            self.students[grade].append(name)


    def roster(self):
        """Returns roster of students"""
        sorted_students = []
        sorted_grades = sorted(list(self.students))
        for grade in sorted_grades:
            sorted_students.extend(sorted(list(self.students[grade])))
        return sorted_students

    def grade(self, grade_number):
        """Returns sorted students in grade"""
        if grade_number not in self.students:
            self.students[grade_number] = []
        return sorted(self.students[grade_number])

    def added(self):
        """Returns history of students added successfully"""
        return self.added_history
