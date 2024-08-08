# Define the student record structure
class Student:
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses

# Define the course record structure
class Course:
    def __init__(self, id, name, credit_hours, grade_points):
        self.id = id
        self.name = name
        self.credit_hours = credit_hours
        self.grade_points = grade_points

# Define the student transaction record structure
class StudentTransaction:
    def __init__(self, id, student_id, course_id, grade):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.grade = grade

# Define the student data access object
class StudentDAO:
    def __init__(self, filename):
        self.filename = filename

    def read_student(self, id):
        # Read the student record from the file
        pass

    def write_student(self, student):
        # Write the student record to the file
        pass

# Define the student transaction data access object
class StudentTransactionDAO:
    def __init__(self, filename):
        self.filename = filename

    def read_student_transaction(self, id):
        # Read the student transaction record from the file
        pass

    def write_student_transaction(self, transaction):
        # Write the student transaction record to the file
        pass

# Define the program logic
def calculate_grade_point_average(student_id):
    # Retrieve the student's course records from the database
    student_dao = StudentDAO("STUDENT.DAT")
    student = student_dao.read_student(student_id)
    if student is None:
        print("Student not found")
        return

    # Calculate the grade point average
    total_grade_points = 0
    total_credit_hours = 0
    for course in student.courses:
        total_grade_points += course.grade_points * course.credit_hours
        total_credit_hours += course.credit_hours

    grade_point_average = total_grade_points / total_credit_hours
    print(f"Grade point average: {grade_point_average}")

# Example usage
calculate_grade_point_average("12345")