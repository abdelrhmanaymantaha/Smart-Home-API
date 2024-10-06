from fastapi import Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from app import models, oauth2
from app.database import get_db
from app import schemas

router= APIRouter(prefix="/sensors",tags=["Sensors"])


@ router.get('',status_code=status.HTTP_200_OK)
def show_all_sensors(db:Session = Depends(get_db),userdata:str = Depends(oauth2.get_cureent_user)):
    sensors_list = db.query(models.IotDevices).all()
    sorted_sensors_list = sorted(sensors_list,key = lambda x : x.id)
    return sorted_sensors_list

@ router.post("",response_model=schemas.SensorOut,status_code=status.HTTP_201_CREATED)
def Add_new_sensor(new_sensor:schemas.AddedSensor,db:Session = Depends(get_db),userdata:str = Depends(oauth2.get_cureent_user)):

    if userdata.admin == False:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"user: {userdata.username} you are not an Admin")
    else:
        exist_sensor = db.query(models.IotDevices).filter(models.IotDevices.id == new_sensor.id).first()
        if exist_sensor:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"Sensor with Id: {new_sensor.id} already exist")
        
        new_sensor =models.IotDevices(** new_sensor.model_dump())
        db.add(new_sensor)
        db.commit()
        db.refresh(new_sensor)
        return new_sensor 


@ router.put("/status/{id}",response_model=schemas.SensorOut)
def edit_sensor_state(id:int,sensor_edit:schemas.SensorUpdateState,db:Session = Depends(get_db),userdata:str = Depends(oauth2.get_cureent_user)):

    querry = db.query(models.IotDevices).filter(models.IotDevices.id == id)
    sensor = querry.first()
#check if the sensor with id is exist or not
    if sensor == None:  
# if the sensor not exist send a code the represent an ERROR
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail=f"Error id:{id} Not found")
    else:
        querry.update(sensor_edit.model_dump())
        db.commit()
    return querry.first()

# @router.delete('')
# def delete_sensor(id)



