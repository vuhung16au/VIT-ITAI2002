# Activity 6: Verify Your Environment Setup

**Objective:** Run a few quick checks to ensure your entire environment is set up correctly and ready for the coursework.

## 1. Verify Python & Virtual Environment
Open your terminal, ensure your virtual environment (`.venv`) is activated, and run:
```bash
python --version
```
- **Expected Result:** `Python 3.14.x`

Check if the libraries are installed:
```bash
python -c "import pandas, numpy, sklearn, matplotlib, seaborn, tensorflow, keras, pgmpy, gym; print('All libraries imported successfully!')"
```
- **Expected Result:** The text "All libraries imported successfully!" is printed. If you get a `ModuleNotFoundError`, ensure your virtual environment is active and you ran the `pip install` command from Activity 1.

## 2. Verify VS Code
Open VS Code, create a file named `check.py`, and look at the bottom right corner of the window (or click `Ctrl+Shift+P` -> `Python: Select Interpreter`). 
- **Expected Result:** It should show the Python version with `('.venv': venv)` next to it, indicating it's using your isolated environment.

## 3. Verify Git and GitHub
Run this in your terminal:
```bash
git --version
gh auth status
```
- **Expected Result:** Git prints its version. The GitHub CLI (`gh`) should say you are logged in.

## 4. Verify Docker and PostgreSQL
Ensure Docker Desktop is running, then run:
```bash
docker ps
```
- **Expected Result:** You should see a container named `itai2002-postgres` with the image `postgres:18.4-alpine` and status "Up".

*(Optional)* Test the database connection using Python:
```bash
pip install psycopg2-binary
python -c "import psycopg2; conn = psycopg2.connect('dbname=itaidb user=admin password=secretpassword host=localhost'); print('Database connected!'); conn.close()"
```
- **Expected Result:** "Database connected!"

## 5. Verify AI Agents
- **If using Copilot:** Start typing a comment like `# Function to calculate fibonacci` in VS Code. It should start suggesting grey text.
- **If using Cursor:** Press `Ctrl+K` (or `Cmd+K`) and type "write a hello world function". It should generate the code.

**If all checks pass, congratulations! Your environment is perfectly set up for the semester.**
