from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/")
def list_projects():
	return {"message": "List of projects"}