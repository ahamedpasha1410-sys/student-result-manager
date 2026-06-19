SUBJECTS = (
    "Python",
    "Database",
    "Networks",
    "Cloud"
)

students = []


def add_student(name, marks):

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)


def get_students():

    return students

def delete_student(name):

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            return True

    return False

def edit_student(name, new_marks):

    for student in students:

        if student["name"].lower() == name.lower():

            student["marks"] = new_marks

            return True

    return False


class Student:

    def __init__(self, student_id, name):

        self.student_id = student_id

        self.name = name

    def display(self):

        return f"{self.student_id} {self.name}"


class StudentCollection:

    def __init__(self, students):

        self.students = students

    def __iter__(self):

        return iter(self.students)  
        return f"{self.student_id} {self.name}"