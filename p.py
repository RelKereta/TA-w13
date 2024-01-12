class Course:
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.current_students = 0

    def enroll(self, student):
        if self.current_students < self.max_capacity:
            self.current_students += 1
            student.enroll(self)
        else:
            raise ValueError("This course is full.")

    def display_details(self):
        return f"{self.course_code}: {self.title} (Capacity: {self.max_capacity}, Enrolled: {self.current_students})"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []

    def enroll(self, course):
        self.courses_enrolled.append(course)

    def display_details(self):
        enrolled_courses = ', '.join([course.title for course in self.courses_enrolled])
        return f"{self.student_id}: {self.name} (Courses: {enrolled_courses})"


def save_data(file_name, data):
    with open(file_name, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


def load_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data


def load_courses(file_name):
    courses = []
    for line in load_data(file_name):
        course_code, title, max_capacity, current_students = line.split(',')
        course = Course(course_code, title, int(max_capacity))
        course.current_students = int(current_students)  
        courses.append(course)
    return courses


def load_students(file_name):
    students = []
    for line in load_data(file_name):
        student_id, name, enrolled_courses = line.split(',')
        student = Student(student_id, name)
        for course_code in enrolled_courses.split(';'):
            for course in courses:
                if course.course_code == course_code:
                    student.enroll(course)
                    break
        students.append(student)
    return students


def display_course_details(courses):
    for course in courses:
        print(course.display_details())


def display_student_details(students):
    for student in students:
        print(student.display_details())


def main():
    courses = load_courses('courses.txt')
    students = load_students('students.txt')

    # Display initial details
    print("Initial Course Details:")
    display_course_details(courses)
    print("\nInitial Student Details:")
    display_student_details(students)

    # Test enrollment
    student = students[0]
    course = courses[0]

    try:
        course.enroll(student)
        print("\nEnrollment successful.")
    except ValueError as e:
        print(f"\nEnrollment failed: {e}")

    # Display updated details
    print("\nUpdated Course Details:")
    display_course_details(courses)
    print("\nUpdated Student Details:")
    display_student_details(students)

    # Save updated data to files
    save_data('courses.txt', [f"{course.course_code},{course.title},{course.max_capacity},{course.current_students}" for course in courses])
    save_data('students.txt', [f"{student.student_id},{student.name},{';'.join([course.course_code for course in student.courses_enrolled])}" for student in students])


if __name__ == "__main__":
    main()
