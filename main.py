from student import (
    add_student,
    get_students,
    edit_student,
    delete_student
)

from utils import (
    find_topper,
    sort_students,
    summarize_results
)
from student import SUBJECTS

def menu():
    while True:   # LOOP concept
        print("1. Add Student")

        print("2. View Students")

        print("3. Edit Student")

        print("4. Delete Student")

        print("5. Find Topper")

        print("6. Sort Students")

        print("7. Summarize Results")

        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            marks = list(map(int, input("Marks (space separated): ").split()))
            add_student(name, marks)

        elif choice == "2":
            for s in get_students():
                print(s)

        elif choice == "3":

           name = input("Student name: ")

           marks = list(
               map(
                   int,
                   input(
                     "New marks: "
                    ).split()
                )
           )

           if edit_student(name, marks):

               print("Updated successfully")

           else:

               print("Student not found")
        elif choice == "4":

            name = input("Student name: ")

            if delete_student(name):

                print("Deleted successfully")

            else:

                print("Student not found")


        elif choice == "5":

             print(
                  "Topper:",
                  find_topper()
            )

        elif choice == "6":

             sort_students()

             print("Sorted!")
        
        elif choice == "7":

             print(

                 summarize_results()

            )
             
        elif choice == "8":

           break
        

menu()