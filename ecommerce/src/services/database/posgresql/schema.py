from pydantic import BaseModel, Field

class SignUpSchema(BaseModel):
    user_id: int = Field(default=None)
    email: str
    password: str
    name: str
    phone: str
    access_token: str = Field(default=None)
    refresh_token: str = Field(default=None)

class SignInSchema(BaseModel):
    email: str
    password: str