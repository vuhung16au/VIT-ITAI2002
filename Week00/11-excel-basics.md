# Activity 11: Using Microsoft Excel for Data Prep

**Objective:** Get comfortable using Microsoft Excel for quick data exploration and basic data cleaning before moving to Python and Pandas.

While we will use Python for heavy data manipulation, Excel remains an industry-standard tool for quickly viewing, understanding, and performing initial cleanups on datasets.

## Step 1: Getting Excel
As a student, you have access to Microsoft 365 for free.
1. Go to [office.com](https://www.office.com/).
2. Sign in with your `.edu.au` university email.
3. You can use Excel for the Web directly in your browser, or click **Install apps** in the top right to download the desktop version (recommended for larger datasets).

## Step 2: Viewing and Exploring Data
When you receive a new dataset (often as a `.csv` or `.xlsx` file), Excel is a great place to do a "sanity check".

- **Opening CSV Files:** Go to `File > Open` and select your CSV. If the data is all squished into one column, go to the `Data` tab and use `Text to Columns` (choose "Delimited" and select Comma).
- **Freeze Panes:** If you have many rows, it's helpful to keep the header row visible as you scroll down. Go to `View > Freeze Panes > Freeze Top Row`.
- **Filtering:** Highlight your header row, go to the `Data` tab, and click `Filter`. You will now have dropdown arrows on each column to easily filter out blanks, view unique values, or search for specific text.
- **Sorting:** Use the same filter dropdowns to sort numerical data (Largest to Smallest) or alphabetical data (A to Z) to spot outliers.

## Step 3: Basic Data Cleaning
Sometimes it is faster to fix glaring data issues in Excel before importing the data into Python.

- **Remove Duplicates:** Select your data range, go to the `Data` tab, and click `Remove Duplicates`. It will ask which columns to check for duplicate values.
- **Find and Replace:** Press `Ctrl + H` (or `Cmd + H`). This is incredibly useful for replacing missing data indicators (like "N/A", "?", or "NULL") with actual blank cells.
- **The TRIM Function:** If your data has weird spacing issues (e.g., `"  Apple "` instead of `"Apple"`), you can create a new column and use the formula `=TRIM(A2)` to clean the text.
- **Changing Data Types:** If numbers are being treated as text (often indicated by a small green triangle in the corner of the cell), highlight them, click the warning icon that appears, and select "Convert to Number".

## When to use Excel vs Python?
- **Use Excel:** For a quick look at the data structure, fixing a couple of obvious typos, or sharing small data summaries with non-technical team members.
- **Use Python (Pandas):** For datasets with hundreds of thousands of rows (which crash Excel), complex transformations, merging multiple tables, and creating automated, repeatable data pipelines.
