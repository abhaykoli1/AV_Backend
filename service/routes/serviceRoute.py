import json
from bson import ObjectId
from fastapi import FastAPI ,APIRouter

from service.models.serviceModel import ServiceJsonModel,ServiceTable

router= APIRouter()
   
@router.post("/api/v1/addService")
async def addService(body : ServiceJsonModel):
    serviceData = ServiceTable(**body.dict())
    serviceData.save()
    toJson = serviceData.to_json()
    fromJson = json.loads(toJson)
    return{
        "message" : "data added successfully",
        "status" : True,
        "data" :  fromJson
    }
    

@router.get("/api/v1/serviceList")
async def serviceList():
    serviceListData = ServiceTable.objects.all()
    toJson = serviceListData.to_json()
    fromJson = json.loads(toJson)
    if(serviceListData): 
      return{
        "message" : "Data Fetched Successfully",
        "status" : True,
        "data" : fromJson,
    }
    else:
       return{
          "message" : "Data Not Found",
          "status" : False,
          "data": None
       }
       

@router.delete("/api/v1/deleteAllServices")
async def deleteServices():
   deleteServiceData = ServiceTable.objects.delete()
   if deleteServiceData == 0:
      return{
         "message" : "data Deleted Successfully",
         "status" : True,
         "data" : None
      }
   
@router.delete("/api/v1/deleteById/{_id}")
async def deleteById(_id : str):
    object_id = ObjectId(_id)
    item = ServiceTable.objects(id=object_id).first()
    item.delete()

    return {
        "message": "Data Deleted Successfully",
        "status": True,
    }