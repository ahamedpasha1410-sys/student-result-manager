students = []

def add_student(name, marks):
    students.append({
        "name": name,
        "marks": marks
    })


def get_students():
    return students

class StudentCollection:

    def __init__(self, students):

        self.students = students

    def __iter__(self):

        return iter(self.students)    