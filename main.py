from clases import Student, Course, Teacher, Grade, SchoolSystem

school_system = SchoolSystem()

course1 = school_system.create_course("Biology",101)
course2 = school_system.create_course("Maths",101)

student1 = school_system.create_student("Brenda Godoy",42840011)
student2 = school_system.create_student("Federico Zurita",34721292)
student3 = school_system.create_student("Lola Zurita",2589631)

student1.register_course(course1)
student1.register_course(course2)
student2.register_course(course1)

grade1 = school_system.create_grade(student1,course1,10)
grade2 = school_system.create_grade(student2,course1,9)
grade3 = school_system.create_grade(student1,course2,7)

# school_system.show_grades_for_student(student1)
# school_system.show_average_grade_for_student(student1)
# school_system.show_average_grade_for_course(course1)

teacher1 = school_system.create_teacher("Ana Godoy", 987654321)
teacher1.register_course(course1)
teacher1.register_course(course2)