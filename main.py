
students= []
    
while True:
    print("\n===== STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")
    print("4. Search Student ")

    choice = int(input("Choose: "))
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))
        student = {
           "name": name,
           "age": age,
           "gpa": gpa
        }
        students.append(student)

    elif choice == 2:

        if len(students) == 0:
            print("No students found")

        else:
            print("\nStudent List:")


            for student in students:
             print(student["name"])
             print(student["age"])
             print(student["gpa"])

    elif choice == 3:

        print("Goodbye")
        break
    elif choice == 4:
         searchname = input("Enter student name: ")
         found = False
 
         for student in students:

            if student["name"] == searchname:

               found = True

               for key, value in student.items():
                print(key, value)

         if not found:
               print("Student not found")
        
        
    else:

        print("Invalid choice")



