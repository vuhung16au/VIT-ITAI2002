# Activity 7: Cloud-Based Jupyter Notebooks (SaaS)

**Objective:** Learn how to use cloud-based Jupyter Notebook platforms like Google Colab and Kaggle. These platforms allow you to run Python code in the browser without installing anything locally, and they provide free access to powerful hardware (like GPUs).

## Option A: Google Colab

Google Colab (Colaboratory) is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud.

1. **Accessing Colab:** Go to [colab.research.google.com](https://colab.research.google.com/). You will need a Google account (your standard Gmail or university Google Workspace account will work).
2. **Creating a Notebook:** Click on **File > New notebook**. 
3. **Running Code:** You can type Python code into the cells. Press `Shift + Enter` to run the cell. The required libraries for this course (like `pandas`, `numpy`, `scikit-learn`, `tensorflow`) are pre-installed in Colab!
4. **Using Free GPUs:** For deep learning tasks, you can speed up execution by using a GPU.
   - Go to **Runtime > Change runtime type**.
   - Under "Hardware accelerator", select **GPU (T4)**.
   - Click **Save**.

## Option B: Kaggle Notebooks

Kaggle is the world's largest data science community, offering powerful notebooks and access to thousands of public datasets.

1. **Create an Account:** Go to [kaggle.com](https://www.kaggle.com/) and click **Register**. You can sign in with your Google account or email.
2. **Creating a Notebook:**
   - Click on the **Create** button (+) on the left sidebar and select **New Notebook**.
   - Kaggle notebooks look and act very much like standard Jupyter Notebooks.
3. **Running Code:** Type your Python code in a cell and press `Shift + Enter` to execute it. Like Colab, Kaggle has all major data science and machine learning libraries pre-installed.
4. **Using Free GPUs:**
   - Look for the **Notebook Options** panel on the right side of the screen.
   - Under **ACCELERATOR**, change the setting from "None" to **GPU T4x2** (or similar available option).
5. **Adding Datasets:** Kaggle makes it incredibly easy to use data. Click **Add Data** on the right panel to search the Kaggle database and instantly mount a dataset to your notebook environment.

*Note: While running code locally (as set up in Activities 1-4) is best for large projects and software engineering practices, Colab and Kaggle are excellent for quick experiments, heavy machine learning training, and completing assignments on any computer.*
