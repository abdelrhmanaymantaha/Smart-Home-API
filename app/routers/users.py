from fastapi import Response,status,HTTPException,Depends,APIRouter

from app import models, schemas, utils
from app.database import get_db
from sqlalchemy.orm import Session

router= APIRouter(prefix="/users",tags=["Users"])

@router.post("",response_model=schemas.UserOut,status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.User,db:Session = Depends(get_db)):
    exist_user = db.query(models.User).filter(models.User.email == user.email).first()
    if exist_user:
      raise HTTPException(detail="This email already exist",status_code=status.HTTP_409_CONFLICT)
    else:
      hashed_password= utils.hash(user.password)
      user.password = hashed_password
      new_user =models.User(** user.dict())
      user = db.query(models.User).filter(models.User.username == new_user.username).first()
      if user :
            raise HTTPException(detail="This user already exist",status_code=status.HTTP_409_CONFLICT)
      else:
          db.add(new_user)
          db.commit()
          db.refresh(new_user)
          return new_user