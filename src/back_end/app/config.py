import os

class Settings:
	DATABASE_URL: os.getenv(
		"DATABASE_URL",
		"postgresql+psycopg2://user:password@localhost:5432/mydatabase",
	)

settings = Settings()