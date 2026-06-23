def add_student():
    name = input("Enter name: ")
    if name.strip() == "":
        print("Name cannot be empty")
        return

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Age must be a number")
        return

    try:
        gpa = float(input("Enter GPA: "))
    except ValueError:
        print("GPA must be a number")
        return

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{gpa}\n")

    print("Student added successfully")


def show_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No students found")
        else:
            print("\nStudent List:")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("No students found")


def search_student():
    search_name = input("Enter student name: ")
    if search_name.strip() == "":
        print("Name cannot be empty")
        return

    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == search_name:
                    print()
                    print("Name:", data[0])
                    print("Age:", data[1])
                    print("GPA:", data[2])
                    found = True
    except FileNotFoundError:
        print("No students found")
        return

    if not found:
        print("Student not found")


def delete_student():
    delete_name = input("Enter student name to delete: ")
    if delete_name.strip() == "":
        print("Name cannot be empty")
        return

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        found = False
        remaining = []

        for line in lines:
            data = line.strip().split(",")
            if data[0] != delete_name:
                remaining.append(line)
            else:
                found = True

        if not found:
            print("Student not found")
            return

        with open("students.txt", "w") as file:
            file.writelines(remaining)

        print(f"Student '{delete_name}' deleted successfully")

    except FileNotFoundError:
        print("No students found")


def update_gpa():
    update_name = input("Enter student name to update GPA: ")
    if update_name.strip() == "":
        print("Name cannot be empty")
        return

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        found = False
        updated = []

        for line in lines:
            data = line.strip().split(",")
            if data[0] == update_name:
                print(f"Current GPA: {data[2]}")
                try:
                    new_gpa = float(input("Enter new GPA: "))
                except ValueError:
                    print("GPA must be a number")
                    return
                updated.append(f"{data[0]},{data[1]},{new_gpa}\n")
                found = True
            else:
                updated.append(line)

        if not found:
            print("Student not found")
            return

        with open("students.txt", "w") as file:
            file.writelines(updated)

        print(f"GPA of '{update_name}' updated successfully")

    except FileNotFoundError:
        print("No students found")


while True:
    print("\n===== STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update GPA")
    print("6. Exit")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        update_gpa()
    elif choice == 6:
        print("Goodbye")
        break
    else:
        print("Invalid choice")


