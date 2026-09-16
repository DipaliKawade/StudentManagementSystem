from Model.stdmodel import StudentStruct
from Database.stddbconn import collection

def CreateStudent(Student: StudentStruct):
    sroll = Student.roll
    sname = Student.name
    sage = Student.age

    sinfo = {
        "roll": sroll,
        "name": sname,
        "age": sage
    }

    collection.insert_one(sinfo)

    return {"message": "Student Created"}