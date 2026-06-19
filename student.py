SUBJECTS = (
    "Python",
    "Database",
    "Networks",
    "Cloud"
)

students = []

def add_student(name, marks):
    students.append({
        "name": name,
        "marks": marks
    })


def get_students():
    return students