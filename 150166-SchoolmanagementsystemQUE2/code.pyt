class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_students(self):
        if not self.students:
            print("No students in the classroom.")
        else:
            for student in self.students:
                print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                average = student.get_average_grade()
                print(f"{student.name}'s average grade: {average}")
                return
        print(f"No student found with the name {name}.")

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades available for the subject {subject}.")
            return 0
        average = total / count
        print(f"Class average for {subject}: {average}")
        return average


def main():
    classroom = Classroom()

    while True:
        print("\nClass Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Get average grade of a student")
        print("4. Get class average for a subject")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            student = Student(name)
            while True:
                add_grade = input("Do you want to add a grade for this student? (yes/no): ").lower()
                if add_grade == 'yes':
                    subject = input("Enter subject: ")
                    grade = float(input("Enter grade: "))
                    student.add_grade(subject, grade)
                else:
                    break
            classroom.add_student(student)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            name = input("Enter the name of the student to get their average grade: ")
            classroom.get_student_average(name)
        elif choice == '4':
            subject = input("Enter the subject to get the class average: ")
            classroom.get_class_average(subject)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
