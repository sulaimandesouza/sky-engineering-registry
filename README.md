# Sky Engineering Registry

A full-stack Django web application developed as a university group project to provide a centralised registry for engineering teams, staff, skills and team dependencies.

The application replaces a manual spreadsheet-based approach with a web-based system featuring authentication, role-based access, team management and relational data.

## Features

* Team directory with search functionality
* Team profiles containing:

  * Department
  * Team leader
  * Engineers
  * Skills
  * Team email
  * Active/inactive status
  * Upstream and downstream team dependencies
* User authentication and role-based access control
* Relational data management using Django ORM
* SQLite database for local development
* Responsive web interface
* Modular Django application structure

## Technology

* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML, CSS, Bootstrap
* **Development:** Git, GitHub

## Project Structure

```text
skyeng/
├── accounts/            # Authentication and user management
├── messages_app/        # Messaging functionality
├── reports_app/         # Reports functionality
├── schedule_app/        # Schedule functionality
├── teams_app/           # Team directory and team management
├── skyeng/              # Django project configuration
├── static/              # CSS and image assets
├── templates/           # Shared templates
├── manage.py
├── requirements.txt
├── README.md
```

## My Contribution

This was a university group project developed collaboratively using Git and feature branches.

My primary responsibility was the **Teams** functionality. I worked on the team's data model and the implementation of the team directory and team detail views.

My work included:

* Designing and implementing the `Department`, `Team` and `Engineer` models
* Implementing relationships between teams, departments and engineers using Django ORM
* Implementing team search functionality
* Developing the team directory and team detail pages
* Displaying team members, skills and team leadership information
* Implementing upstream and downstream team dependency relationships
* Adding team status and contact information
* Creating reusable demo data through Django fixtures
* Working with Git feature branches and integrating changes into the group repository

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/sulaimandesouza/sky-engineering-registry.git
cd sky-engineering-registry/skyeng
```

### 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Load demo team data

```bash
python manage.py loaddata teams_demo.json
```

This loads example departments, teams and engineers used to demonstrate the Teams functionality.

### 6. Start the development server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

## Demo Data

The repository includes a Django fixture containing example engineering departments, teams and engineers.

The fixture can be loaded with:

```bash
python manage.py loaddata teams_demo.json
```

The database itself is intentionally excluded from version control. This allows each developer to create a fresh local database using the project's migrations and demo fixture.

## Project Context

This application was developed for the **5COSC021W Software Development Group Project** at the University of Westminster.

The project was developed collaboratively using Git, with team members working on separate application areas and integrating their work into the main branch.

