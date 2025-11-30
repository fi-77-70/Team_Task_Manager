from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from app.models import Base

class ProjectMember(Base):
	__tablename__ = "project_members"

	project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
	role = Column(String(20), default="member")
	joined_at = Column(TIMESTAMP, server_default="NOW()")
