# Activity 2: Setup Visual Studio Code (VS Code)

**Objective:** Install and configure Visual Studio Code, our highly recommended and primary IDE for this course.

## Step 1: Install VS Code

- **Windows, macOS, and Linux:**
  1. Go to the [Visual Studio Code download page](https://code.visualstudio.com/).
  2. Download the installer for your specific operating system (always get the latest stable version).
  3. Run the installer and follow the standard installation prompts. 
     - *Tip for Windows:* Ensure "Add to PATH" is checked during installation.

## Step 2: Install Essential Extensions

VS Code is a lightweight editor that gains its power from extensions. Open VS Code and click on the **Extensions** view icon on the left sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`).

Search for and install the following extensions:
1. **Python** (by Microsoft): Essential for Python support, linting, and debugging.
2. **Jupyter** (by Microsoft): Required for running Jupyter Notebooks (`.ipynb` files) directly inside VS Code.
3. *(Optional but recommended)* **Pylance** (by Microsoft): Provides fast and feature-rich Python language support.

## Step 3: Configure VS Code to use your Virtual Environment

To ensure VS Code uses the packages you installed in Activity 1:

1. Open your course folder (`ITAI2002-Projects`) in VS Code by going to `File > Open Folder...`.
2. Open any Python file (e.g., create a `test.py` file) or a Jupyter Notebook.
3. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
4. Type and select **Python: Select Interpreter**.
5. You should see an option that points to the `.venv` folder you created in Activity 1 (e.g., `./.venv/bin/python` or `.\.venv\Scripts\python.exe`). Select it.

VS Code will now use this isolated environment for running your code and providing autocomplete suggestions!
