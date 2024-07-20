## Table of Contents
- [Description](#description)
- [Design System](#design-system)
- [Installation Backend](#installation-backend)
- [Installation Frontend](#installation-frontend)
- [Contributing](#contributing)
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
python manage.py langchain_stream
```
### Test the Setup
Start the Django development server:
```cmd
python manage.py runserver
```




