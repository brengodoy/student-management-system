class Student():
    def __init__(self,full_name,student_id):
        self.full_name = full_name
        self.student_id = student_id
        self.courses = []
        
    def enroll_in_course(self,course):
        self.courses.append(course)
        course.students_registered.append(self)
        
    def show_student_data(self):
        print("Student's name: " + self.full_name)
        print("Student's ID: " + str(self.student_id))
        print("This student is registered in:")
        for course in self.courses:
            print(course.name)
            
    def show_all_grades(self):
        print("All the grades of this student are: ")
        for grade in all_grades:
            for course in self.courses:
                if grade.student.full_name == self.full_name and course.name == grade.course.name:
                    print("Course: " + course.name)
                    print("Grade: " + str(grade.grade))
                    
    def show_average_grade(self):
        count = 0
        total = 0
        for grade in all_grades:
            for course in self.courses:
                if grade.student.full_name == self.full_name and course.name == grade.course.name:
                    total += grade.grade
                    count += 1
        avg = total / count
        print("Grade average is: " + str(avg))
        
class Course():
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.students_registered = []
        self.teacher = None
        
    def show_course_data(self):
        print("Course name: " + self.name)
        print("Course code: " + str(self.code))
        print("The students registered in this course are:")
        for student in self.students_registered:
            print(student.full_name)
         
    def show_average_grade_course(self):
        count = 0
        total = 0
        for grade in all_grades:
            if grade.course.name == self.name:
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
        
    def show_teacher_data(self):
        print("Teahcer's name: " + self.full_name)
        print("Teahcer's id: " + self.teacher_id)
        print("This teacher teaches in:")
        for course in self.courses:
            print(course.name)

class Grade():
    def __init__(self,student,course,grade):
        self.student = student
        self.course = course
        self.grade = grade

all_grades = []
course1 = Course("Biology",101)
course2 = Course("Maths",101)
student1 = Student("Brenda Godoy",42840011)
student2 = Student("Federico Zurita",34721292)
student1.enroll_in_course(course1)
student2.enroll_in_course(course1)
student1.enroll_in_course(course2)
course1.show_course_data()
print(" ")
student1.show_student_data()
grade1 = Grade(student1,course1,10)
grade3 = Grade(student2,course1,9)
grade2 = Grade(student1,course2,7)
all_grades.append(grade1)
all_grades.append(grade2)
all_grades.append(grade3)
student1.show_all_grades()
student1.show_average_grade()
course1.show_average_grade_course()