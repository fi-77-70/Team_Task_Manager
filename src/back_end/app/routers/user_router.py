from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from werkzeug.security import generate_password_hash  # optional, simple hashing

router = APIRouter(prefix="/users", tags=["Users"])

# Create user endpoint
@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password
    hashed_password = generate_password_hash(user.password)
    
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# List all users
@router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Get user by ID
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
	user = db.query(User).filter(User.id == user_id).first()
	if not user:
		raise HTTPException(status_code=404, detail="User not found")
	return user

# Update user by ID
@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
	user = db.query(User).filter(User.id == user_id).first()
	if not user:
		raise HTTPException(status_code=404, detail="User not found")
	
	# Update fields
	user.name = user_update.name
	user.email = user_update.email
	user.password_hash = generate_password_hash(user_update.password)
	
	db.commit()
	db.refresh(user)
	return user

# Delete user by ID
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
	user = db.query(User).filter(User.id == user_id).first()
	if not user:
		raise HTTPException(status_code=404, detail="User not found")
	
	db.delete(user)
	db.commit()
	return {"detail": "User deleted successfully"}

#TODO : Add The rest of the end points and routers for the other models
