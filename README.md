# 🎓 Student Management System

Este es un proyecto simple en Python para gestionar estudiantes, profesores, cursos y calificaciones en una institución educativa. Fue desarrollado como práctica de Programación Orientada a Objetos, con foco en herencia, encapsulamiento y relaciones entre clases.

## 🚀 Funcionalidades

- Registrar estudiantes, profesores y cursos.
- Asignar profesores a cursos.
- Inscribir estudiantes en cursos.
- Registrar calificaciones.
- Mostrar todas las notas de un estudiante.
- Calcular promedios por estudiante o por curso.

## 🧠 Clases principales

- `Person`: Clase base para `Student` y `Teacher`.
- `Student`: Hereda de `Person`. Puede registrarse en cursos.
- `Teacher`: Hereda de `Person`. Puede enseñar cursos.
- `Course`: Contiene información sobre un curso, estudiantes inscriptos y su profesor.
- `Grade`: Representa una nota asociada a un estudiante y un curso.
- `SchoolSystem`: Administra las entidades anteriores.

## 📁 Estructura

- `clases.py`: Contiene todas las clases del sistema.
- (Opcional) `main.py`: Podés crear un script para probar el sistema con inputs o ejemplos.

## 💻 Ejemplo de uso

```python
from clases import *

school = SchoolSystem()

# Crear estudiantes y cursos
student1 = school.create_student("Brenda Godoy", 78654125)
course1 = school.create_course("Python 101", "PY101")

# Registrar al estudiante en el curso
student1.register_course(course1)

# Agregar nota
grade1 = school.create_grade(student1, course1, 9.5)

# Ver notas
school.show_grades_for_student(student1)
```


## ✨ Tecnologías
- Python 3.x
- Paradigma de Programación Orientada a Objetos (OOP)

## 👩‍💻 Sobre mí
Este proyecto fue desarrollado por Brenda Godoy como parte de su camino en la programación, buscando aprender, mejorar y compartir su progreso con el mundo 🌍.
Sígueme para más proyectos, y contenido tech 💖
