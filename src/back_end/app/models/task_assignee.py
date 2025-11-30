from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from app.models import Base

class TaskAssignee(Base):
    __tablename__ = "task_assignees"

    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    assigned_at = Column(TIMESTAMP, server_default="NOW()")
