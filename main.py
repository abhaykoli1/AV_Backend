from fastapi import FastAPI,APIRouter
from mongoengine import connect
from service.routes import serviceRoute
connect('AVBIGBUDDYSITE', host="mongodb+srv://avbigbuddy:nZ4ATPTwJjzYnm20@cluster0.wplpkxz.mongodb.net/AVBIGBUDDYSITE")


app = FastAPI()
app.include_router(serviceRoute.router, tags=["Service"])

import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080 , reload = True)
