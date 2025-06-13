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
            
    def show_all_grades(self):
        print("All the grades of this student are: ")
        for grade in all_grades:
            for course in self.courses:
                if grade.student == self and course.code == grade.course.code:
                    print("Course: " + course.name)
                    print("Grade: " + str(grade.grade))
                    
    def show_average_grade(self):
        count = 0
        total = 0
        for grade in all_grades:
            for course in self.courses:
                if grade.student == self and course.code == grade.course.code:
                    total += grade.grade
                    count += 1
        if count == 0:
            print("No grades available.")
        else:
            avg = total / count
            print("Grade average is: " + str(avg))
        
class Course():
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.students_registered = []
        self.teacher = None
            
    def __str__(self):
        students_str = "\n".join([student.full_name for student in self.students_registered])
        return (f'Course name: {self.name}\nCourse code: {self.code}\nThe students registered in this course are:\n{students_str}')
         
    def show_average_grade_course(self):
        count = 0
        total = 0
        for grade in all_grades:
            if grade.course == self:
                total += grade.grade
                count += 1
        avg = total / count
        print("Grade average is: " + str(avg))
         
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

all_grades = []
course1 = Course("Biology",101)
course2 = Course("Maths",101)
student1 = Student("Brenda Godoy",42840011)
student2 = Student("Federico Zurita",34721292)
student1.enroll_in_course(course1)
student2.enroll_in_course(course1)
student1.enroll_in_course(course2)
#course1.show_course_data()
#print(" ")
#student1.show_student_data()
#print(student1)
#print(course1)
grade1 = Grade(student1,course1,10)
grade3 = Grade(student2,course1,9)
grade2 = Grade(student1,course2,7)
all_grades.append(grade1)
all_grades.append(grade2)
all_grades.append(grade3)
# student1.show_all_grades()
# student1.show_average_grade()
# course1.show_average_grade_course()
teacher1 = Teacher("Ana Godoy", 987654321)
teacher1.teaches_in_course(course1)
#print(teacher1)
print(grade1)