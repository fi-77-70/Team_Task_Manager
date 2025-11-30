-- =================
-- USERS
-- =================

CREATE TABLE users (
	id				SERIAL PRIMARY KEY,
	name			VARCHAR(100) NOT NULL UNIQUE,
	email			VARCHAR(100) NOT NULL UNIQUE,
	password_hash	VARCHAR(255) NOT NULL,
	created_at		TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =================
-- Projects
-- =================

CREATE TABLE projects (
	id				SERIAL PRIMARY KEY,
	name			VARCHAR(100) NOT NULL,
	description		TEXT,
	created_by		INT REFERENCES users(id) ON DELETE SET NULL,
	created_at		TIMESTAMP DEFAULT NOW()
);

-- =================
-- PROJECT MEMBERS
-- =================

CREATE TABLE project_members (
	project_id		INT REFERENCES projects(id) ON DELETE CASCADE,
	user_id	INT 	REFERENCES users(id) ON DELETE CASCADE,
	role			VARCHAR(50) DEFAULT 'member',
	joined_at		TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (project_id, user_id)
);

-- =================
-- TASKS
-- =================

CREATE TABLE tasks (
	id	SERIAL PRIMARY KEY,
	project_id		INT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
	parent_task_id	INT REFERENCES tasks(id) ON DELETE CASCADE, -- for sub tasks
	title			VARCHAR(200) NOT NULL,
	description		TEXT,
	status			VARCHAR(50) DEFAULT 'pending', -- pending/ongoing/completed
	urgent			BOOLEAN DEFAULT FALSE,
	created_by		INT REFERENCES users(id) ON DELETE SET NULL,
	assigned_to		INT REFERENCES users(id) ON DELETE SET NULL,
	created_at		TIMESTAMP DEFAULT NOW(),
	started_at		TIMESTAMP,
	completed_at	TIMESTAMP
);

-- =================
-- TASK ASSIGNEES
-- =================

CREATE TABLE task_assignees (
	task_id	INT REFERENCES tasks(id) ON DELETE CASCADE,
	user_id	INT REFERENCES users(id) ON DELETE CASCADE,
	assigned_at	TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (task_id, user_id)
);