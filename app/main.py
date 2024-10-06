from fastapi import FastAPI

from app.routers import auth, sensorsAPI, users
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
  
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, or specify your domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
) 
 
@ app.get("/")
def testing():
   return {"message":"Wellcome in Smart Home API"}

app.include_router(sensorsAPI.router)
app.include_router(users.router)
app.include_router(auth.router)