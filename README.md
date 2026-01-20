# A01_OPIM5512_kgm19004
Repository: `A01 - first OPIM assignment`

The purpose of this assignment is to become familiar with GitHub (web interface and GitHub desktop), including making a repository, cloning it locally, and executing a simple python script to generate running a box plot.

# Data used
This assignment uses the **California Housing** dataset. The following variables are included:

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Average Occupation
* Latitude
* Longitude
* Median House Value
  
For this assignment, the box plot is created using the **house age** variable.

# How to run the script
The script is executed in **Visual Studio Code** using **Python**, with the repository managed through **GitHub Desktop**.
  1. Clone the repository using GitHub Desktop.
  2. Open the project in Visual Studio Code.
  3. Run the Python script from the integrated terminal.

**Methods**
* Dataset loaded into Python and returned as a **pandas DataFrame**.
* `panda`s is used for data manipulation.
* `matplotlib.pyplot` is used to generate the box plot.
* DataFrame (`df`) contains eight feature variables and one target variable (median house value).
* A preliminary data check is performed to confirm successful data loading and structure.

**Box plot generation:**
* Specifying figure size (12 x 8).
* Selecting the **house age** column for visualization.
* Adding descriptive plot title and y-label.
* Saving the resulting figure to the `figs` directory within the repository

# Expected Output
The expected output is a saved box plot visualizing the **house age**. The plot displays:
* Minimum and maximum values (lower and upper whiskers)
* Median value (green central line)
* 25th and 75th percentiles (lower and upper edges of the box)

The visualization provides a concise summary of the distribution and variability of house age in the data set.
