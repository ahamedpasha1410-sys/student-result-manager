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