from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#Request schema for creating a project_meber
class ProjectMemberCreate(BaseModel):
	project_id: int
	user_id: int
	role: Optional[str] = "member"

#Response schema for project_member data
class ProjectMemberRead(BaseModel):
	project_id: int
	user_id: int
	role: str
	joined_at: Optional[datetime]

	class Config:
		orm_mode = True