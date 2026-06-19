# 🎓 Student Result Manager

## Project Overview

Student Result Manager is a Python-based command line application that helps manage student records and perform result-related operations.

The project demonstrates real-world usage of Python fundamentals along with Git and Pull Request workflows.

This project was intentionally built by implementing Python concepts such as:

* Lists
* Tuples
* Iterables
* Iterators
* Loops
* Functions
* Conditional statements
* Git branching
* Pull Requests

---

## Features

* Add students
* View all students
* Find class topper
* Sort students based on marks
* Display available subjects
* Implement iterable student collections
* Implement custom iterators

---

## Technologies Used

* Python
* Git
* GitHub
* Virtual Environment (venv)

---

## Project Structure

```text
student-result-manager/

main.py
student.py
utils.py
README.md
.gitignore
venv/
```

---

# File Explanation

## main.py

This file controls the entire application.

It provides a menu-driven interface.

Available operations:

1. Add Student
2. View Students
3. Find Topper
4. Sort Students
5. Exit

### Operations happening

### Add Student

User enters:

* Name
* Marks

Data is stored inside a student list.

### View Students

Displays all student records.

### Find Topper

Calculates totals and identifies the highest-scoring student.

### Sort Students

Sorts students according to total marks.

### Exit

Terminates the application.

---

## student.py

This file stores student-related data and logic.

### Components

### SUBJECTS Tuple

```python
SUBJECTS = (
    "Python",
    "Database",
    "Networks",
    "Cloud"
)
```

Purpose:

* Stores fixed subjects
* Demonstrates tuple usage
* Tuples are immutable

---

### students List

```python
students = []
```

Purpose:

Stores all student records.

Example:

```python
[
  {
    "name": "Ahmed",
    "marks": [90,85,95]
  }
]
```

---

### add_student()

Adds a student to the list.

Operation:

```python
append()
```

is used.

---

### get_students()

Returns all student records.

---

### Student Class

Stores:

* student_id
* student_name

Methods:

```python
display()
```

Returns formatted student information.

---

### StudentCollection

Purpose:

Implements Python iterable concepts.

```python
__iter__()
```

allows:

```python
for student in collection:
    print(student)
```

---

## utils.py

This file contains utility functions.

### calculate_total()

Calculates total marks.

Operation:

```python
sum()
```

---

### find_topper()

Loops through all students.

Compares total marks.

Returns the highest scorer.

---

### sort_students()

Uses manual swapping.

```python
students[i], students[j] = students[j], students[i]
```

Sorts students in descending order.

---

### RankIterator

Custom iterator implementation.

Methods:

```python
__iter__()

__next__()
```

Python automatically uses these methods while iterating.

---

# Python Concepts Implemented

## Lists

```python
students = []
```

Purpose:

Store dynamic student data.

---

## Tuples

```python
SUBJECTS = (
   "Python",
   "Database",
   "Networks",
   "Cloud"
)
```

Purpose:

Store fixed data.

---

## Iterables

```python
class StudentCollection
```

Purpose:

Make collections loopable.

---

## Iterators

```python
class RankIterator
```

Purpose:

Traverse data one element at a time.

---

## Loops

Used throughout the application.

Examples:

```python
for

while
```

---

## Conditions

Used for menu navigation.

```python
if

elif

else
```

---

# Pull Request Workflow

## PR1

Title:

Implement student management system

### Changes

* Added student management functionality
* Added student data handling
* Added menu operations

### Need

Created the core functionality of the application.

---

## PR2

Title:

Add tuple based subject management

### Changes

* Added SUBJECTS tuple
* Displayed available subjects

### Need

Introduced immutable data structures.

---

## PR3

Title:

Implement iterable student collection

### Changes

* Added StudentCollection
* Added **iter**()

### Need

Introduced iterable concepts.

---

## PR4

Title:

Implement custom rank iterator for student ranking

### Changes

* Added RankIterator
* Added **iter**()
* Added **next**()

### Need

Introduced iterator concepts.

---

# Git Workflow Followed

```text
main

├── feature/student-management

├── feature/subject-tuples

├── feature/student-iterable

└── feature/rank-iterator
```

Each feature was developed independently and merged into main using Pull Requests.

---

# Learning Outcomes

After completing this project, I learned:

* Python data structures
* Object-oriented programming
* Iterables and iterators
* Git branching
* Pull Request workflows
* Project organization
* Version control best practices

```
```
