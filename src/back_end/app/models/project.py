from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP, ForeignKey
from app.models import Base

class Project(Base):
	__tablename__ = "projects"

	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	description = Column(TEXT)
	created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
	created_at = Column(TIMESTAMP, server_default="NOW()")