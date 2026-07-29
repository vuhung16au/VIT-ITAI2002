# Activity 1: Setup Python Environment

**Objective:** Install Python 3.14 and configure a virtual environment with the required libraries for this course.

## Step 1: Install Python 3.14

We require Python 3.14 for this course.

- **Windows:** 
  1. Download the Windows installer for Python 3.14 from the [official Python website](https://www.python.org/downloads/).
  2. Run the installer. **CRITICAL:** Make sure to check the box that says **"Add Python 3.14 to PATH"** at the bottom of the installation window before clicking "Install Now".
- **macOS:**
  1. Download the macOS installer from the [official Python website](https://www.python.org/downloads/).
  2. Run the installer and follow the prompts.
  3. *(Alternative)* Use Homebrew: `brew install python@3.14`
- **Linux (Ubuntu/Debian):**
  Open a terminal and run:
  ```bash
  sudo apt update
  sudo apt install python3.14 python3.14-venv python3-pip
  ```

Verify installation by opening a terminal/command prompt and typing:
```bash
python --version
```
*(On some macOS/Linux systems, you may need to use `python3 --version`)*

## Step 2: Create a Virtual Environment

Virtual environments keep your course project isolated from other projects on your computer.

1. Create a folder for the course on your computer (e.g., `ITAI2002-Projects`) and navigate into it using your terminal:
   ```bash
   mkdir ITAI2002-Projects
   cd ITAI2002-Projects
   ```
2. Create the virtual environment (named `.venv`):
   ```bash
   python -m venv .venv
   ```
   *(Use `python3` if `python` doesn't work)*

3. Activate the virtual environment:
   - **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   - **macOS/Linux:** `source .venv/bin/activate`

You will know it's activated when you see `(.venv)` at the beginning of your terminal prompt.

## Step 3: Install Required Libraries

With your virtual environment activated, install the core libraries required for the course:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn tensorflow keras pgmpy gym
```

*Note: For the complete exhaustive list of libraries, refer to the `techstack.md` document in the course repository.*

**You are now ready to write Python code!** Proceed to the next activity.
