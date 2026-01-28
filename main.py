from models import Student, Teacher

# addition of teachers
Teacher.create(name="Ravi", subject="Math")
Teacher.create(name="Neha", subject="Science")

# addition of students
Student.create(name="Aman", grade=10, teacher_id=2)
Student.create(name="Harshita", grade=7, teacher_id=1)

print(Student.objects().filter(grade=10))
print(Student.get_teacher(1))

Student.objects().update({"name": "Aman"}, grade=9)
Student.objects().delete(name="Harshita")

print(Student.objects().all())