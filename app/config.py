from pydantic_settings import BaseSettings
 

# this file used for valided the env variables 
class Settings(BaseSettings):
    DATABASE_USERNAME : str
    DATABASE_PASSWORD : int
    DATABASE_PORT : int
    DATABASE_NAME : str
    DATABASE_HOSTNAME : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES_SMART_HOME : int
    class Config:
        env_file = '.env_smarthome'


settings = Settings()