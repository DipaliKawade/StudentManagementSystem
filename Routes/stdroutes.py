from fastapi import APIRouter
from Controller.stdcontroller import CreateStudent 
from Model.stdmodel import StudentStruct
from Model.stdUpdate import updateStruct
from Database.stddbconn import collection

router = APIRouter()

@router.post("/createStudent")
def create(student:StudentStruct):
    return CreateStudent(student)

@router.get("/allstudents")
def GetStudent():
    alldata = list(collection.find({},{"_id":0}))
    return alldata


@router.put("/edit/{roll}")
def UpdateStudent(roll:int,student:updateStruct):
    alldata = list(collection.find({},{"_id":0}))

    updatedstudent = {}

    for i in alldata:
        if i["roll"]==roll:

            if student.name != None:
                updatedstudent["name"]=student.name

            if student.age != None:
                updatedstudent["age"] = student.age

        collection.update_one(
            {"roll":roll},
            {"$set":updatedstudent}
        )

        return {"message":"student Updated"}



@router.delete("/delete/{roll}")
def Deletstudent(roll:int):
    alldata = list(collection.find({},{"_id":0}))

    for i in alldata:
        if i["roll"]==roll:
            collection.delete_one({"roll":roll})
            return {"message":"student deleted"}
    