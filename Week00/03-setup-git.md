# Activity 3: Setup Git and GitHub

**Objective:** Get familiar with version control by setting up Git, GitHub, the GitHub CLI, and GitHub Desktop.

## Step 1: Create a GitHub Account
If you don't already have one, go to [GitHub](https://github.com/) and sign up for a free account. **Tip:** Use your `.edu.au` email address to access student benefits later!

## Step 2: Install Git (Core Version Control)

- **Windows:** Download and install [Git for Windows](https://gitforwindows.org/).
- **macOS:** Open a terminal and type `git --version`. If it's not installed, macOS will prompt you to install Xcode Command Line Tools. Alternatively, install via Homebrew: `brew install git`.
- **Linux (Ubuntu/Debian):** `sudo apt install git`

**Configure Git:**
Open your terminal/command prompt and set your identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Install GitHub CLI (`gh`) (Optional but Powerful)

The GitHub CLI allows you to create repositories and manage PRs right from the terminal.

- **Windows:** `winget install --id GitHub.cli` (or download the installer from [cli.github.com](https://cli.github.com/)).
- **macOS:** `brew install gh`
- **Linux:** Follow the instructions on the [GitHub CLI page](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

**Authenticate:** Run `gh auth login` in your terminal and follow the interactive prompts to link it to your GitHub account.

## Step 4: Install GitHub Desktop (Visual Client)

If you prefer a graphical user interface over the command line:
1. Download [GitHub Desktop](https://desktop.github.com/).
2. Install and launch the application.
3. Go to **File > Options** (Windows) or **GitHub Desktop > Preferences** (macOS) and sign in to your GitHub account.

## Step 5: GitHub Extension for VS Code

To integrate GitHub directly into your editor:
1. Open VS Code.
2. Go to Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`).
3. Search for and install **GitHub Pull Requests and Issues** (by GitHub).
4. Click the new GitHub icon on the left sidebar and follow the prompts to sign in.
