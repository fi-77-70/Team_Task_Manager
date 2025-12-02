from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.project_member import ProjectMember
from datetime import datetime
from app.schemas.project_member import ProjectMemberCreate, ProjectMemberRead

router = APIRouter(prefix="/project_members", tags=["Project Members"])

@router.get("/", response_model=list[ProjectMemberRead])
def list_project_members(db: Session = Depends(get_db)):
	project_members = db.query(ProjectMember).all()
	return project_members

@router.post("/", response_model=ProjectMemberRead)
def create_project_member(project_member: ProjectMemberCreate, db: Session = Depends(get_db)):
    new_project_member = ProjectMember(
        project_id=project_member.project_id,
        user_id=project_member.user_id,
        role=project_member.role or "member",
        joined_at=datetime.now()  # automatically set the timestamp
    )
    db.add(new_project_member)
    db.commit()
    db.refresh(new_project_member)
    return new_project_member

@router.get("/{project_id}/{user_id}", response_model=ProjectMemberRead)
def get_project_member(project_id: int, user_id: int, db: Session = Depends(get_db)):
	project_member = db.query(ProjectMember).filter(
		ProjectMember.project_id == project_id,
		ProjectMember.user_id == user_id
	).first()
	if not project_member:
		raise HTTPException(status_code=404, detail="Project member not found")
	return project_member

@router.put("/{project_id}/{user_id}", response_model=ProjectMemberRead)
def update_project_member(project_id: int, user_id: int, project_member_update: ProjectMemberCreate, db: Session = Depends(get_db)):
	project_member = db.query(ProjectMember).filter(
		ProjectMember.project_id == project_id,
		ProjectMember.user_id == user_id
	).first()
	if not project_member:
		raise HTTPException(status_code=404, detail="Project member not found")
	
	# Update fields
	project_member.role = project_member_update.role
	project_member.joined_at = project_member_update.joined_at
	
	db.commit()
	db.refresh(project_member)
	return project_member

@router.delete("/{project_id}/{user_id}")
def delete_project_member(project_id: int, user_id: int, db: Session = Depends(get_db)):
	project_member = db.query(ProjectMember).filter(
		ProjectMember.project_id == project_id,
		ProjectMember.user_id == user_id
	).first()
	if not project_member:
		raise HTTPException(status_code=404, detail="Project member not found")
	
	db.delete(project_member)
	db.commit()
	return {"detail": "Project member deleted successfully"}

