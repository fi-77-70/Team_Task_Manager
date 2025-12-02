from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.project_router import router as project_router
from app.routers.task_router import router as task_router
from app.routers.project_member_router import router as project_member_router
from app.routers.task_assinee_router import router as task_assignee_router


app = FastAPI(title="Team Task Manager API")

app.include_router(user_router)
app.include_router(project_router)
app.include_router(task_router)
app.include_router(project_member_router)
app.include_router(task_assignee_router)

@app.get("/")
def root():
	return {"message": "Team Task Manager API is running!"}