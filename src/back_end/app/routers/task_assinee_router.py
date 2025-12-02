from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.task_assignee import TaskAssignee
from app.schemas.task_assignee import TaskAssigneeCreate, TaskAssigneeRead

router = APIRouter(prefix="/task_assignees", tags=["Task Assignees"])

@router.get("/{id}", response_model=list[TaskAssigneeRead])
def list_task_assignees(id: int, db: Session = Depends(get_db)):
	task_assignees = db.query(TaskAssignee).filter(TaskAssignee.task_id == id).all()
	return task_assignees

@router.post("/", response_model=TaskAssigneeRead)
def create_task_assignee(task_assignee: TaskAssigneeCreate, db: Session = Depends(get_db)):
	new_task_assignee = TaskAssignee(
		task_id=task_assignee.task_id,
		user_id=task_assignee.user_id,
		assigned_at=task_assignee.assigned_at
	)
	db.add(new_task_assignee)
	db.commit()
	db.refresh(new_task_assignee)
	return new_task_assignee

@router.delete("/{task_id}/{user_id}")
def delete_task_assignee(task_id: int, user_id: int, db: Session = Depends(get_db)):
	task_assignee = db.query(TaskAssignee).filter(
		TaskAssignee.task_id == task_id,
		TaskAssignee.user_id == user_id
	).first()
	if not task_assignee:
		raise HTTPException(status_code=404, detail="Task assignee not found")
	
	db.delete(task_assignee)
	db.commit()
	return {"detail": "Task assignee deleted successfully"}

@router.get("/{task_id}/{user_id}", response_model=TaskAssigneeRead)
def get_task_assignee(task_id: int, user_id: int, db: Session = Depends(get_db)):
	task_assignee = db.query(TaskAssignee).filter(
		TaskAssignee.task_id == task_id,
		TaskAssignee.user_id == user_id
	).first()
	if not task_assignee:
		raise HTTPException(status_code=404, detail="Task assignee not found")
	return task_assignee

@router.put("/{task_id}/{user_id}", response_model=TaskAssigneeRead)
def update_task_assignee(task_id: int, user_id: int, task_assignee_update: TaskAssigneeCreate, db: Session = Depends(get_db)):
	task_assignee = db.query(TaskAssignee).filter(
		TaskAssignee.task_id == task_id,
		TaskAssignee.user_id == user_id
	).first()
	if not task_assignee:
		raise HTTPException(status_code=404, detail="Task assignee not found")
	
	# Update fields
	task_assignee.assigned_at = task_assignee_update.assigned_at
	
	db.commit
	db.refresh(task_assignee)
	return task_assignee

@router.delete("/{task_id}/{user_id}")
def delete_task_assignee(task_id: int, user_id: int, db: Session = Depends(get_db)):
	task_assignee = db.query(TaskAssignee).filter(
		TaskAssignee.task_id == task_id,
		TaskAssignee.user_id == user_id
	).first()
	if not task_assignee:
		raise HTTPException(status_code=404, detail="Task assignee not found")
	
	db.delete(task_assignee)
	db.commit()
	return {"detail": "Task assignee deleted successfully"}