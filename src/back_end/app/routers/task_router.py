from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead


router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
	tasks = db.query(Task).all()
	return tasks

@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
	new_task = Task(
		project_id=task.project_id,
		parent_task_id=task.parent_task_id,
		title=task.title,
		description=task.description,
		status=task.status,
		created_by=task.created_by,
		assigned_to=task.assigned_to
	)
	db.add(new_task)
	db.commit()
	db.refresh(new_task)
	return task

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, db: Session = Depends(get_db)):
	task = db.query(Task).filter(Task.id == task_id).first()
	if not task:
		raise HTTPException(status_code=404, detail="Task not found")
	return task

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
	task = db.query(Task).filter(Task.id == task_id).first()
	if not task:
		raise HTTPException(status_code=404, detail="Task not found")
	
	# Update fields
	task.title = task_update.title
	task.description = task_update.description
	task.status = task_update.status
	task.assigned_to = task_update.assigned_to

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
	task = db.query(Task).filter(Task.id == task_id).first()
	if not task:
		raise HTTPException(status_code=404, detail="Task not found")
	
	db.delete(task)
	db.commit()
	return {"detail": "Task deleted successfully"}

