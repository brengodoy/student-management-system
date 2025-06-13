from clases import Student, Course, Teacher, Grade, System

system = System()

course1 = Course("Biology",101)
course2 = Course("Maths",101)
system.add_course(course1)
system.add_course(course2)

student1 = Student("Brenda Godoy",42840011)
student2 = Student("Federico Zurita",34721292)
system.add_student(student1)
system.add_student(student2)

student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)

grade1 = Grade(student1,course1,10)
grade2 = Grade(student2,course1,9)
grade3 = Grade(student1,course2,7)
system.add_grade(grade1)
system.add_grade(grade2)
system.add_grade(grade3)

system.show_grades_for_student(student1)
system.show_average_grade_for_student(student1)
system.show_average_grade_for_course(course1)

teacher1 = Teacher("Ana Godoy", 987654321)
system.add_teacher(teacher1)
teacher1.teaches_in_course(course1)