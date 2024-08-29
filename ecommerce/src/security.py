from os import getenv
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
import jwt
from datetime import timedelta,datetime,timezone

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="./token")

SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ENCRYPTION_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generate_access_token(data:dict, exp_in_min: int):
    payload_data = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=exp_in_min)
    payload_data['exp'] = expiry_time
    access_token = jwt.encode(payload_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return access_token

def generate_refresh_token(data:dict, exp_in_min: int):
    payload_data = data.copy()
    expiry_time = datetime.now(timezone.utc) + timedelta(minutes=exp_in_min)
    payload_data['exp'] = expiry_time
    refresh_token = jwt.encode(payload_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return refresh_token

def get_user(access_token : Annotated[str, Depends(oauth2_scheme)]):
    try:
        return jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
    except:
        raise HTTPException(status_code=401, detail='UNAUTHORIZED: Access Denied')