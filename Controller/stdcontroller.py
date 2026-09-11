from Model.stdmodel import StudentStruct
from Database.stddbconn import collection


def CreateStudent(student:StudentStruct):
    sroll = student.roll_no
    sname = student.name
    sage = student.age


    sinfo = {

        "roll_no" : sroll,
        "name" : sname,
        "age" : sage
    }

    collection.insert_one(sinfo)

    return {"message":"student created"}


def GetStudent():
    alldata = list(collection.find({},{"_id":0}))
    return alldata