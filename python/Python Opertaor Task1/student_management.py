class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name, grade):
        self.courses.append((course_name, grade))

    def display_details(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print("Enrolled Courses:")
        for course, grade in self.courses:
            print(f" - {course}: {grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_name, student_id):
        if any(student.student_id == student_id for student in self.students):
            print("Error: Student ID already exists!")
            return
        student = Student(student_name, student_id)  # Corrected instantiation
        self.students.append(student)
        print("Student added successfully!")

    def enroll_student(self, student_id, course_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.enroll_course(course_name, grade)
            print("Student enrolled in course successfully!")
        else:
            print("Error: Student ID not found!")

    def list_all_students(self):
        if not self.students:
            print("No students registered.")
        else:
            print("\nList of students:")
            for student in self.students:
                print(f" - {student.student_name} (ID: {student.student_id})")

    def view_student_courses(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.display_details()
        else:
            print("Error: Student ID not found!")

    def main(self):
        while True:
            print("\nStudent Record Management System")
            print("1. Add a new student")
            print("2. Enroll a student in a course")
            print("3. View student courses")
            print("4. List all students")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                self.add_student(name, student_id)

            elif choice == "2":
                student_id = input("Enter student ID: ")
                course_name = input("Enter course name: ")
                grade = input("Enter grade: ")
                self.enroll_student(student_id, course_name, grade)

            elif choice == "3":
                student_id = input("Enter student ID: ")
                self.view_student_courses(student_id)

            elif choice == "4":
                self.list_all_students()

            elif choice == "5":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice! Please enter a valid option between 1 and 5.")




StudentManagementSystem.main()
    


        

