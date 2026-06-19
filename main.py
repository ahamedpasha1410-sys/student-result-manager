from student import add_student, get_students
from utils import find_topper, sort_students
from student import SUBJECTS

def menu():
    while True:   # LOOP concept
        print("\n--- Student System ---")
        print("Subjects:", ", ".join(SUBJECTS))
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Topper")
        print("4. Sort Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            marks = list(map(int, input("Marks (space separated): ").split()))
            add_student(name, marks)

        elif choice == "2":
            for s in get_students():
                print(s)

        elif choice == "3":
            print("Topper:", find_topper())

        elif choice == "4":
            sort_students()
            print("Sorted!")

        elif choice == "5":
            break

        else:
            print("Invalid choice")

menu()