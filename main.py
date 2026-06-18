students = []

def add_student(name, marks):
    students.append((name, marks))

def calculate_result(student):
    name, marks = student
    total = sum(marks)
    average = total / len(marks)
    return name, total, average

def display_results():
    print("\n--- Student Results ---\n")

    for student in students:
        name, total, avg = calculate_result(student)
        print(f"{name} | Total: {total} | Avg: {avg:.2f}")

def iterator_demo():
    print("\n--- Iterator Demo ---")

    it = iter(students)

    while True:
        try:
            student = next(it)
            print("Processing:", student[0])
        except StopIteration:
            break

add_student("Alice", [85, 90, 88])
add_student("Bob", [70, 65, 75])
add_student("Charlie", [95, 92, 96])

display_results()
iterator_demo()