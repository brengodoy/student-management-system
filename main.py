from clases import Student, Course, Teacher, Grade, SchoolSystem

school_system = SchoolSystem()

course1 = Course("Biology",101)
course2 = Course("Maths",101)
school_system.add_course(course1)
school_system.add_course(course2)

student1 = Student("Brenda Godoy",42840011)
student2 = Student("Federico Zurita",34721292)
student3 = Student("Lola Zurita",2589631)
school_system.add_student(student1)
school_system.add_student(student2)
school_system.add_student(student3)

student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)

grade1 = Grade(student1,course1,10)
grade2 = Grade(student2,course1,9)
grade3 = Grade(student1,course2,7)
school_system.add_grade(grade1)
school_system.add_grade(grade2)
school_system.add_grade(grade3)

school_system.show_grades_for_student(student1)
# school_system.show_average_grade_for_student(student1)
# school_system.show_average_grade_for_course(course1)

teacher1 = Teacher("Ana Godoy", 987654321)
school_system.add_teacher(teacher1)
teacher1.teaches_in_course(course1)
teacher1.teaches_in_course(course2)