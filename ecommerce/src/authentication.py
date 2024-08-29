from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from passlib.context import CryptContext
from sqlalchemy.sql import select
from .services.database.postgresql.database import SessionLocal
from .services.database.postgresql.schema import SignUpSchema, SignInSchema
from .services.database.postgresql.models import User
from .services.database.postgresql import models
from .services.database.postgresql.database import engine
from .security import generate_access_token,generate_refresh_token

auth_router=APIRouter(prefix='/auth', tags=['auth'])

models.Base.metadata.create_all(bind=engine)

session = SessionLocal()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_router.post('/signup')
async def signUp(user:SignUpSchema):
    try:
        user_detail=session.query(User).filter(User.email==user.email).first()

        if user_detail is not None:
            raise HTTPException(status_code=401, detail='BAD REQUEST: User already exist')
    except:
        pass
    new_user = User(
                email=user.email,
                password=pwd_context.hash(user.password),
                name=user.name,
                phone=user.phone
            )
    session.add(new_user)
    session.commit()

    return new_user

@auth_router.post('/signin')
async def signIn(user:SignInSchema):

    user_detail = session.query(User).filter(User.email==user.email).first()

    if user_detail and pwd_context.verify(user.password, user_detail.password):
        payload_data={
            "user_id":user_detail.user_id,
            "email":user_detail.email
        }

        access = generate_access_token(payload_data, 1)
        refresh = generate_refresh_token(payload_data, 1)

        user_detail.access_token = access
        user_detail.refresh_token = refresh
        session.commit()
        
        return {
            "access":access,
            "refresh":refresh
        }
    else:
        raise HTTPException(status_code=400, detail='INVAILD USER: Invalid user details.')