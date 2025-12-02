from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#Request schema for creating a task
class TaskCreate(BaseModel):
	project_id: int
	parent_task_id: Optional[int] = None
	title: str
	description: Optional[str] = None
	status: Optional[str] = "pending"
	created_by: Optional[int] = None

#Response schema for task data
class TaskRead(BaseModel):
	id: int
	project_id: int
	parent_task_id: Optional[int]
	title: str
	description: Optional[str]
	status: str
	created_by: Optional[int]
	assigned_to: Optional[int]
	created_at: Optional[datetime]
	started_at: Optional[datetime]
	completed_at: Optional[datetime]

	class Config:
		orm_mode = True