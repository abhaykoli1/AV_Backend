from mongoengine import Document,StringField,IntField
from pydantic import BaseModel

class ServiceTable(Document):
    image = StringField(required = True)
    title = StringField(required =True)
    description = StringField(required =True)

class ServiceJsonModel(BaseModel):
    image : str 
    title : str
    description : str 