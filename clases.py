class Student():
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        
    def enroll_in_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.students_registered.append(self)
            return f"Student {self.name} enrolled correctly in {course.name}."
        else:
            return f"The student {self.name} is already enrolled in {course.name}."
            
    def __str__(self):
        if self.courses:
            courses_str = '\n'.join([course.name for course in self.courses])
            message = f"This student is registered in:\n{courses_str}" 
        else:
            message = "This student isn't registered in any courses."
        return (f"Student's name: {self.name}\nStudent's ID: {self.student_id}\n{message}")
        
class Course():
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.students_registered = []
        self.teacher = None
            
    def __str__(self):
        if self.students_registered:
            students_str = "\n".join([student.name for student in self.students_registered])
            message = f"The students registered in this course are:\n{students_str}"
        else:
            message = "There are no students registered in this course."
        return (f'Course name: {self.name}\nCourse code: {self.code}\n{message}')
         
class Teacher():
    def __init__(self,full_name,teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id
        self.courses = []
    
    def teaches_in_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            course.teacher = self
            return f"Teacher {self.full_name} was registered correctly in {course.name}."
        else:
            return f"The teacher {self.full_name} already teaches in {course.name}."
            
    def __str__(self):
        if self.courses:
            courses_str = "\n".join([course.name for course in self.courses])
            message = f"This teacher teaches in:\n{courses_str}"
        else:
            message = "This teacher doesn't teaches in any courses yet."
        return (f"Teacher's name: {self.full_name}\nTeacher's id: {self.teacher_id}\n{message}")

class Grade():
    def __init__(self,student,course,grade):
        self.student = student
        self.course = course
        self.grade = grade
        
    def __str__(self):
        return (f"Student: {self.student.name}\nCourse: {self.course.name}\nGrade: {self.grade}")
    
class SchoolSystem():
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
        grades_student = []
        for grade in self.grades:
            if grade.student == student:
                grades_student.append(grade)
        if grades_student:
            print(f"All the grades of {student.name} are: ")
            for grade in grades_student:
                print(f'Course: {grade.course.name}. Grade: {str(grade.grade)}')
        else:
            print(f"There are no grades for {student.name} yet.")
                
    def show_average_grade_for_student(self,student):
        avg = self.calculate_average(student)
        self.show_avg(avg,student)
            
    def show_average_grade_for_course(self,course):
        avg = self.calculate_average(course)
        self.show_avg(avg,course)
            
    def calculate_average(self,instance):
        count = total = 0
        for grade in self.grades:
            if isinstance(instance,Student):
                if grade.student == instance:
                    total += grade.grade
                    count += 1
            elif isinstance(instance,Course):
                if grade.course == instance:
                    total += grade.grade
                    count += 1
        if count == 0:
            return None
        else:
            return total / count
    
    def show_avg(self,avg,instance):
        if avg is None:
            print(f"No grades available for {instance.name}.")
        else:
            print(f"Grade average for {instance.name} is: {str(avg)}")