class Person():
    def __init__(self,name,identifier):
        self.name = name
        self.identifier = identifier
        self.courses = []
        
    def __str__(self):
        if self.courses:
            courses_str = '\n'.join([course.name for course in self.courses])
            message = f"{self.name} is registered in:\n{courses_str}" 
        else:
            message = "This person isn't registered in any courses."
        return (f"Name: {self.name}\nID: {self.identifier}\n{message}")
        
    def register_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} registered correctly in {course.name}."
        else:
            return f"{self.name} is already registered in {course.name}."

class Student(Person):
    def __init__(self,name,identifier):
        super().__init__(name,identifier)
        
    def register_course(self,course):
        msg = super().register_course(course)
        if self not in course.students_registered:
            course.students_registered.append(self)
        return msg
            
    def __str__(self):
        return f"STUDENT'S INFO:\n{super().__str__()}"
        
class Teacher(Person):
    def __init__(self,name,identifier):
        super().__init__(name,identifier)
        
    def __str__(self):
        return f"TEACHER'S INFO:\n{super().__str__()}"
    
    def register_course(self,course):
        if course.teacher is None:
            msg = super().register_course(course)
            course.teacher = self
        else:
            msg = f"This course already has a teacher: {course.teacher.name}"
        return msg
        
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
        if self.teacher:
            teacher_message = f"{self.teacher.name}"
        else:
            teacher_message = f"No teacher assigned."
        return (f'Course name: {self.name}\nCourse code: {self.code}\n{message}\nTeacher: {teacher_message}')

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
        
    def create_student(self,name,identifier):
        student = Student(name,identifier)
        self._add_student(student)
        return student
        
    def _add_student(self,student):
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"{student.name} is already added.")
    
    def create_course(self,name,code):
        course = Course(name,code)
        self._add_course(course)
        return course        
    
    def _add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
        else: 
            print(f"{course.name} is already added.")
        
    def create_teacher(self,name,identifier):
        teacher = Teacher(name,identifier)
        self._add_teacher(teacher)
        return teacher
        
    def _add_teacher(self,teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print(f"{teacher.name} is already added.")
        
    def create_grade(self,student,course,grade):
        grade_var = Grade(student,course,grade)
        self._add_grade(grade_var)
        return grade_var
        
    def _add_grade(self,grade):
        if grade not in self.grades:
            self.grades.append(grade)
        else:
            print(f"{grade} is already added.")
        
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
        grades = [g.grade for g in self.grades if g.student == instance or g.course == instance]
        return sum(grades) / len(grades) if grades else None
    
    def show_avg(self,avg,instance):
        if avg is None:
            print(f"No grades available for {instance.name}.")
        else:
            print(f"Grade average for {instance.name} is: {str(avg)}")