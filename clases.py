class Student():
    def __init__(self,full_name,student_id):
        self.full_name = full_name
        self.student_id = student_id
        self.courses = []
        
    def enroll_in_course(self,course):
        self.courses.append(course)
        course.students_registered.append(self)
            
    def __str__(self):
        courses_str = "\n".join([course.name for course in self.courses])
        return (f"Student's name: {self.full_name}\nStudent's ID: {self.student_id}\nThis student is registered in:\n{courses_str}")
        
class Course():
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.students_registered = []
        self.teacher = None
            
    def __str__(self):
        students_str = "\n".join([student.full_name for student in self.students_registered])
        return (f'Course name: {self.name}\nCourse code: {self.code}\nThe students registered in this course are:\n{students_str}')
         
class Teacher():
    def __init__(self,full_name,teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id
        self.courses = []
    
    def teaches_in_course(self,course):
        self.courses.append(course)
        course.teacher = self
            
    def __str__(self):
        courses_str = "\n".join([course.name for course in self.courses])
        return (f"Teacher's name: {self.full_name}\nTeacher's id: {self.teacher_id}\nThis teacher teaches in:\n{courses_str}")

class Grade():
    def __init__(self,student,course,grade):
        self.student = student
        self.course = course
        self.grade = grade
        
    def __str__(self):
        return (f"Student: {self.student.full_name}\nCourse: {self.course.name}\nGrade: {self.grade}")
    
class System():
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.grades = []
        
    def add_student(self,student):
        self.students.append(student)
        
    def add_course(self,course):
        self.courses.append(course)
        
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
        
    def add_grade(self,grade):
        self.grades.append(grade)
        
    def show_grades_for_student(self,student):
        print(f"All the grades of {student.full_name} are: ")
        for grade in self.grades:
            if grade.student == student:
                print(f'Course: {grade.course.name}. Grade: {str(grade.grade)}')
                
    def show_average_grade_for_student(self,student):
        count = 0
        total = 0
        for grade in self.grades:
            if grade.student == student:
                total += grade.grade
                count += 1
        if count == 0:
            print("No grades available.")
        else:
            avg = total / count
            print(f"Grade average for {student.full_name} is: {str(avg)}")
            
    def show_average_grade_for_course(self,course):
        count = 0
        total = 0
        for grade in self.grades:
            if grade.course == course:
                total += grade.grade
                count += 1
        avg = total / count
        print(f"Grade average for {course.name} is: {str(avg)}")