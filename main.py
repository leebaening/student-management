def add_student():

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gpa = float(input("Enter GPA: "))

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

    found = False

    with open("students.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == search_name:

                print()

                print("Name:", data[0])
                print("Age:", data[1])
                print("GPA:", data[2])

                found = True

    if not found:
        print("Student not found")



    
while True:
    print("\n===== STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")
    print("4. Search Student ")

    choice = int(input("Choose: "))
    if choice == 1:
     add_student()
     

    elif choice == 2:
     show_students()

     

    elif choice == 3:

        print("Goodbye")
        break


    elif choice == 4:
         search_student()
         
        
        
    else:

        print("Invalid choice")



