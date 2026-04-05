---

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

---

**A simple web application written in Python using Flask and SQLAlchemy** to demonstrate Create, Read, Update, and Delete (CRUD) operations on a **SQLite** database.

It is designed as a lightweight demonstration of routing, templates, and Object-Relational Mapping (ORM) using the Flask web framework.

## Use Case
This application is designed for basic web application demonstrations and learning. By providing a fully functional MVC-like structure with basic database interactions, it serves as an excellent starting point for building small-scale applications or understanding web framework foundations in Python.

## Minimum Requirements
To build and execute this project, the following minimum requirements must be met:
- **Python:** `3.8` or higher
- **Package Manager:** `pip` for installing the required dependencies

## Architecture
```mermaid
flowchart TD
    User([User / Web Browser])
    
    subgraph Web App ["Flask Application"]
        Flask["Flask Routes (movie.py)"]
        Templates["Jinja2 Templates (templates/)"]
        Static["Static Assets (static/)"]
    end
    
    subgraph Storage ["Local Storage"]
        SQLite[("SQLite DB (Movies.db)")]
    end
    
    User <-->|HTTP GET/POST| Flask
    Flask <-->|Render HTML| Templates
    Templates --- Static
    Flask <-->|SQLAlchemy ORM| SQLite
```

| Component | Type | Use Case |
| :--- | :--- | :--- |
| **Frontend** | Jinja2 Templates + Static Assets | Renders the HTML interface for users to interact with movies. |
| **Backend** | Flask | Handles the web API endpoints (`/`, `/update`, `/delete`) and core logic. |
| **Database** | SQLite + SQLAlchemy ORM | Local, file-based database handling the persistent storage of movie titles. |

## Tech Stack
- **Backend Framework:** Python, Flask
- **Database & ORM:** SQLite, SQLAlchemy (via Flask-SQLAlchemy)
- **Testing & Security Tooling:** pytest, bandit, safety, python-taint, pylint

## Features
- **Create:** Add new movies to the database via frontend form submission.
- **Read:** Display all added movies on the main page dynamically.
- **Update:** Modify the title of an existing movie.
- **Delete:** Remove a movie from the database.
- **Code Quality:** Configured with several linters, security scanners (`bandit`), and test runners natively.

## Project Structure
```text
.
├── movie.py                    # Main Flask application file and DB models
├── tests/
│   └── test_basic.py           # Unit tests using pytest
├── templates/                  # Directory for Jinja2 HTML templates
├── static/                     # Directory for static files (CSS, JS)
├── requirements.txt            # Python dependencies lists
├── run_bandit.py               # Helper script to run bandit security tests
├── bandit.ignore               # Bandit exclusions configurations
├── sonar-project.properties    # SonarQube static code analysis properties
└── README.md                   # Project documentation
```

## Step-by-Step Execution Guide
Follow these steps precisely to locally deploy and run the application:

### 1. Clone the Repository
Open your terminal and clone the repository, then navigate into the project directory:
```bash
git clone <repository-url>
cd movie-crud-flask
```

### 2. Create a Virtual Environment (Optional but Recommended)
Ensure you isolate your dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all the required Python packages defined in the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```bash
python movie.py
```
*Depending on the configuration, you should be able to access the app at `http://127.0.0.1:5000/` or `http://0.0.0.0:5000/`.*

## Testing & Troubleshooting
To verify the application mechanics:
1. Open a browser and access the host URL. Add a new movie and verify it appears.
2. Attempt to Edit and Delete that entry.
3. **Unit Tests:** Validate application logic by running `pytest test_basic.py`.
4. **Security Tests:** Inspect the codebase by running `python run_bandit.py`.

## Cleanup Procedures
To shut down the app, use `Ctrl+C` in the running terminal. 
To clear database state, safely delete the `Movies.db` SQLite file:
```bash
rm Movies.db
```
To exit the virtual environment, simply run:
```bash
deactivate
```

---

**Manish Pandey** — Senior DevOps/Platform Engineer

### 🛠️ Technology Stack
#### ☁️ Cloud & Platforms
![GCP](https://img.shields.io/badge/GCP-Expert-blue?style=flat-square&logo=google-cloud)
![AWS](https://img.shields.io/badge/AWS-Expert-FF9900?style=flat-square&logo=amazon-aws)

#### ⚙️ Platform & DevOps
![Kubernetes](https://img.shields.io/badge/Kubernetes-Expert-blue?style=flat-square&logo=kubernetes)
![Docker](https://img.shields.io/badge/Docker-Expert-2496ED?style=flat-square&logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-Advanced-7B42BC?style=flat-square&logo=terraform)
![Helm](https://img.shields.io/badge/Helm-Advanced-0F1689?style=flat-square&logo=helm)
![Ansible](https://img.shields.io/badge/Ansible-Expert-EE0000?style=flat-square&logo=ansible)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Expert-green?style=flat-square&logo=github-actions)

#### 🔐 Security & Ops
![IAM](https://img.shields.io/badge/IAM-Expert-red?style=flat-square)
![Networking](https://img.shields.io/badge/Networking-Advanced-blue?style=flat-square)
![Monitoring](https://img.shields.io/badge/Monitoring%20%26%20Logging-Expert-green?style=flat-square&logo=grafana)
![Secrets Management](https://img.shields.io/badge/Secrets%20Mgmt-Advanced-yellow?style=flat-square&logo=vault)

#### 🧑‍💻 Programming
![Python](https://img.shields.io/badge/Python-Advanced-3776AB?style=flat-square&logo=python)
![Bash](https://img.shields.io/badge/Bash-Advanced-4EAA25?style=flat-square&logo=gnu-bash)
![YAML](https://img.shields.io/badge/YAML-Advanced-CB171E?style=flat-square)

#### 💾 Database
![SQL](https://img.shields.io/badge/SQL-Advanced-CC2927?style=flat-square&logo=mysql)
![MongoDB](https://img.shields.io/badge/MongoDB-Advanced-13AA52?style=flat-square&logo=mongodb)

### Connect With Me
- **GitHub:** [@mpandey95](https://github.com/mpandey95)
- **LinkedIn:** [manish-pandey95](https://linkedin.com/in/manish-pandey95)
- **Email:** <mnshkmrpnd@gmail.com>

### License
See **LICENSE** | Support: [GitHub](https://github.com/mpandey95) • [LinkedIn](https://linkedin.com/in/manish-pandey95)