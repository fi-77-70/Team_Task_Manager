from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.project import Project
from app.models.project_member import ProjectMember
from app.schemas.project import ProjectCreate, ProjectRead

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=list[ProjectRead])
def list_user_projects(user_id: int, db: Session = Depends(get_db)):
    # Projects created by the user
    created_projects = db.query(Project).filter(Project.created_by == user_id)
    
    # Projects where the user is a member
    member_projects = db.query(Project).join(ProjectMember).filter(ProjectMember.user_id == user_id)
    
    # Combine queries using union
    projects = created_projects.union(member_projects).all()
    
    return projects

@router.get("/{user_id}", response_model=list[ProjectRead])
def list_user_projects(user_id: int, db: Session = Depends(get_db)):
	projects = db.query(Project).filter(Project.created_by == user_id).all()
	return projects

@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
	new_project = Project(
		name=project.name,
		description=project.description,
		created_by=project.created_by
	)
	db.add(new_project)
	db.commit()
	db.refresh(new_project)
	return new_project

@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
	project = db.query(Project).filter(Project.id == project_id).first()
	if not project:
		raise HTTPException(status_code=404, detail="Project not found")
	return project

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project_update: ProjectCreate, db: Session = Depends(get_db)):
	project = db.query(Project).filter(Project.id == project_id).first()
	if not project:
		raise HTTPException(status_code=404, detail="Project not found")
	
	# Update fields
	project.name = project_update.name
	project.description = project_update.description
	
	db.commit()
	db.refresh(project)
	return project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
	project = db.query(Project).filter(Project.id == project_id).first()
	if not project:
		raise HTTPException(status_code=404, detail="Project not found")
	
	db.delete(project)
	db.commit()
	return {"detail": "Project deleted successfully"}

