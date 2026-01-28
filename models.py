# now as we know ORM's main job is to convert the tables into classes
# so here we do the same 
# students table --> Student class
# teachers table --> Teacher class

from database import database, get_next_id
from query import query_set

# basemodel for all tables(has common logic for all the tables)
# we need basemodel because each table need create(), objects(), so instead of repeating code
class BaseModel:
    table_name = None 

    @classmethod
    def create(cls, **kwargs):
        table = database[cls.table_name]
        kwargs["id"] = get_next_id(table)
        table.append(kwargs)
        return kwargs
    
    @classmethod
    def objects(cls):
        return query_set(database[cls.table_name])


# student and teacher models

class Student(BaseModel):
    table_name = "students"

    # relationship student --> teacher
    # this will simulate the foreign key logic
    @classmethod
    def get_teacher(cls, student_id):
        from models import Teacher
        student = cls.objects().get(id=student_id)
        return Teacher.objects().get(id=student["id"])

class Teacher(BaseModel):
    table_name = "teachers"