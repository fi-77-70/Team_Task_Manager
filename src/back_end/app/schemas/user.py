from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#Request schema for creating a user
class UserCreate(BaseModel):
	name: str
	email: EmailStr
	password: str

#Response schema for user data
class UserRead(BaseModel):
	id: int
	name: str
	email: EmailStr
	created_at: Optional[datetime]

	class Config:
		orm_mode = True