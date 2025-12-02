from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP, ForeignKey
from app.models import Base

class Task(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))
	parent_task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=True)
	title = Column(String(255), nullable=False)
	description = Column(TEXT)
	status = Column(String(20), default="pending")
	created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
	assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
	created_at = Column(TIMESTAMP, server_default="NOW()")
	started_at = Column(TIMESTAMP)
	completed_at = Column(TIMESTAMP)