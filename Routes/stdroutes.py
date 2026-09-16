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
def UpdateStudent(roll: int, student: updateStruct):
    alldata = list(collection.find({}, {"_id": 0}))

    updatedstudent = {}

    for i in alldata:
        if i["roll"] == roll:
            if student.name is not None:
                updatedstudent["name"] = student.name

            if student.age is not None:
                updatedstudent["age"] = student.age

            collection.update_one(
                {"roll": roll},
                {"$set": updatedstudent}
            )

            return {"message": "student Updated"}

    return {"message": "student not found"}



@router.delete("/delete/{roll}")
def Deletstudent(roll: int):
    result = collection.delete_one({"roll": roll})

    if result.deleted_count == 1:
        return {"message": "student deleted"}

    return {"message": "student not found"}