from Model.stdmodel import StudentStruct
from Database.stddbconn import collection


def CreateStudent(Student: StudentStruct):

    sroll = Student.roll
    sname = Student.name
    sage = Student.age
    semail = Student.email

    sinfo = {
        "roll": sroll,
        "name": sname,
        "age": sage,
        "email": semail
    }

    collection.insert_one(sinfo)

    return {"message": "Student Created"}