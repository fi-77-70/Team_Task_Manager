// In docker-compose: your backend is reachable at http://localhost:8000
// Later in Kubernetes: this becomes just /api/
const API = "/api/users";

async function registerUser(userData) {
	const response = await fetch(`${API}/users/`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(userData),
	});
	return response.json();
}

async function login(email, password) {
  const res = await fetch("/api/users/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  
  if (!res.ok) throw new Error("Login failed");
  const user = await res.json();
  localStorage.setItem("user_id", user.id);
  loadProjects(user.id);
}

async function loadProjects(userId) {
  const res = await fetch(`/api/projects/${userId}`);
  const projects = await res.json();
  console.log(projects);  // display in UI
}