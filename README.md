## Table of Contents
- [Description](#description)
- [Design System](#design-system)
- [Installation Backend](#installation-backend)
- [Create Vector Database with PGVector](#vector-database)
- [Installation Frontend](#installation-frontend)
- [Run Application](#run-application)
- [Contact](#contact)

# Description
This project implements a Chatbot using Retrieval-Augmented Generation (RAG) with Django, Websockets, and React.js. The backend, built with Django, handles data retrieval and processing, while real-time communication is facilitated through Websockets. The frontend, developed in React.js, provides an interactive user interface for seamless chatbot interactions.

# Design System
![Desigin System](./design-system.jpg)

# Installation Backend
### Install PGVector

Ensure [C++ support in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170#download-and-install-the-tools) and [PostgreSQL](https://www.postgresql.org/download/windows/) are installed, and run:

```cmd
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

Note: The exact path will vary depending on your Visual Studio version and edition

Then use `nmake` to build:

```cmd
set "PGROOT=C:\Program Files\PostgreQL\16"
cd %TEMP%
git clone --branch v0.7.2 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```
### Create Virtual Environment
Then create new environment where contain nessessary packages to this project.
Ensure you have Python 3.10+ installed.
```cmd
python -m venv .venv
```
Activate new enviroment
```cmd
.venv\Scripts\activate
```
Then, install the required dependencies using pip:
```cmd
pip install -r requirements.txt
```
### Create your Django project
Open your terminal or command prompt and run:
```cmd
django-admin startproject Django_React_Langchain_Stream
```
Then move into the project directory:
```cmd
cd Django_React_Langchain_Stream
```
### Create your Django app
```cmd
python manage.py startapp langchain_stream
```
### Test the Setup
Start the Django development server:
```cmd
python manage.py runserver
```
### Notes
You need to create a .env file to store essential keys for the project such as OPENAI_API_KEY, LANGCHAIN_API_KEY, SECRET_KEY,ALLOWED_HOSTS, APP_DEBUG,  and others.

# Create Vector Database with PGVector
Move into the langchain-stream app directory and run command in your terminal:
```cmd
python rag_load_and_process.py
```
Then wait for the process to complete (it may take a few minutes) and check the database for the new table called "langchain_pg_embeding and langchain_pg_collection" in your PostgreSQL database.

# Installation Frontend
Ensure Node.js and npm are installed
run
```cmd
node -v
npm -v
```
if installed, you should see their version numbers. For example:
```cmd
v20.8.0
10.1.0
```
### Create a React Application
Generate a new React project:
```cmd
npm create vite@latest
```
Name the project frontend, select 'React' as the framework, and choose 'JavaScript' for the variant. Then, navigate into your new frontend directory:

```cmd
cd frontend
```
Install the required React packages:
```cmd
npm install
```

### Test the Frontend
Start the React development server:
```cmd
npm run dev
```
Visit the URL shown in your terminal (usually http://localhost:5173/) to view your React app’s welcome page.

# Run Application
All done! To run the application, start the Django server and the React development server
In 2 separate terminals, make sure you’re in the root directory of your Django project, run:
```cmd
python manage.py runserver
```
and in the frontend directory, run:
```cmd
cd frontend
npm run dev
```
Visit the URL shown in your terminal (usually http://localhost:5173/) to view the app.

# Contact
For questions, contributions, or bug reports, please feel free to reach out:

- Email: [hoangcongtrong02.dut@gmail.com](hoangcongtrong02.dut@gmail.com)
- Linkedin: [https://www.linkedin.com/in/hoangtrong151102/](https://www.linkedin.com/in/hoangtrong151102/)
- Instagram: [https://www.instagram.com/h.c.trong_02/](https://www.instagram.com/h.c.trong_02/)

I appreciate your feedback and involvement!




