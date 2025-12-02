from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#Request schema for creating a project
class ProjectCreate(BaseModel):
	name: str
	description: Optional[str]
	created_by: Optional[int]

#Response schema for project data
class ProjectRead(BaseModel):
	id: int
	name: str
	description: Optional[str]
	created_by: Optional[int]
	created_at: Optional[datetime]

	class Config:
		orm_mode = True