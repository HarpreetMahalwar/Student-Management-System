# List to store all student records
students = []

while True:
    # Display menu
    print("\n===== Student Management Menu =====")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by name")
    print("4. Update marks of a student")
    print("5. Delete a student")
    print("6. Exit")

    # Take user input for menu choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a new student
        name = input("Enter student name: ")
        age_input = input("Enter age: ")
        if not age_input.isdigit():
            print("Invalid age. Must be a number.")
            continue
        age = int(age_input)
        
        subjects_input = input("Enter subjects (comma-separated): ")
        subjects = tuple(subjects_input.split(","))  # tuple of subjects
        
        marks_input = input("Enter marks (comma-separated): ")
        try:
            marks = list(map(int, marks_input.split(",")))  # list of integers
        except ValueError:
            print("Marks must be numbers separated by commas.")
            continue
        
        # Check if number of subjects matches number of marks
        if len(subjects) != len(marks):
            print("Error: Number of subjects and marks do not match!")
            continue
        
        # Create student dictionary
        student = {
            "name": name,
            "age": age,
            "subjects": subjects,
            "marks": marks
        }
        students.append(student)
        print(f"Student {name} added successfully!")

    elif choice == "2":
        # View all students
        if not students:
            print("No students to display.")
            continue
        for idx, s in enumerate(students, start=1):
            print(f"{idx}. Name: {s['name']} | Age: {s['age']} | Subjects: {s['subjects']} | Marks: {s['marks']}")

    elif choice == "3":
        # Search for a student by name
        search_name = input("Enter name to search: ").lower()
        found = False
        for s in students:
            if s["name"].lower() == search_name:
                print(f"Found: Name: {s['name']} | Age: {s['age']} | Subjects: {s['subjects']} | Marks: {s['marks']}")
                found = True
                break  # stop searching after first match
        if not found:
            print("Student not found.")

    elif choice == "4":
        # Update marks of a student
        search_name = input("Enter student name to update marks: ").lower()
        found = False
        for s in students:
            if s["name"].lower() == search_name:
                found = True
                print("Subjects:", s["subjects"])
                subject_to_update = input("Enter subject to update: ")
                if subject_to_update not in s["subjects"]:
                    print("Subject not found!")
                    break
                index = s["subjects"].index(subject_to_update)
                try:
                    new_mark = int(input(f"Enter new mark for {subject_to_update}: "))
                    s["marks"][index] = new_mark
                    print("Marks updated successfully!")
                except ValueError:
                    print("Invalid mark. Must be a number.")
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        # Delete a student
        search_name = input("Enter student name to delete: ").lower()
        found = False
        for s in students:
            if s["name"].lower() == search_name:
                students.remove(s)
                print(f"Student {s['name']} deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        # Exit program
        print("Exiting program... Goodbye!")
        break  # break out of while loop

    else:
        # Invalid choice
        print("Invalid choice! Please enter a number between 1 and 6.")
        continue
                            #Developer : Ch.H.Mahalwar
                            # Last updated : 23/05/2025s