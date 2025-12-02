from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#Request schema for creating a task_assignee
class TaskAssigneeCreate(BaseModel):
	task_id: int
	user_id: int

#Response schema for task_assignee data
class TaskAssigneeRead(BaseModel):
	task_id: int
	user_id: int
	assigned_at: Optional[datetime]

	class Config:
		orm_mode = True