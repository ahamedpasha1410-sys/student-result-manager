from student import students


def calculate_total(student):
    return sum(student["marks"])


def find_topper():
    topper = students[0]

    for student in students:   # LOOP concept
        if calculate_total(student) > calculate_total(topper):
            topper = student

    return topper


# SWAPPING concept (sorting manually)
def sort_students():
    n = len(students)

    for i in range(n):
        for j in range(i + 1, n):
            if calculate_total(students[i]) < calculate_total(students[j]):
                students[i], students[j] = students[j], students[i]  # SWAP


class RankIterator:

    def __init__(self, students):

        self.students = students

        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index >= len(self.students):

            raise StopIteration

        student = self.students[self.index]

        self.index += 1

        return student


def summarize_results():

    if not students:

        return "No students available"

    total_students = len(students)

    highest = 0

    lowest = calculate_total(students[0])

    total_marks = 0

    for student in students:

        marks = calculate_total(student)

        total_marks += marks

        if marks > highest:

            highest = marks

        if marks < lowest:

            lowest = marks

    average = total_marks / total_students

    return {

        "Total Students": total_students,

        "Highest Marks": highest,

        "Lowest Marks": lowest,

        "Average": round(average, 2)

    }
