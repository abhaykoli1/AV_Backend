from mongoengine import Document,StringField,IntField
from pydantic import BaseModel 

class MembersTable(Document):
    image = StringField(required = True)
    name = StringField(required =True)
    designation = StringField(required =True)

class MenbersJsonModel(BaseModel):
    image : str
    name : str
    designation : str 