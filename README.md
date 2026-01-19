# A01_OPIM5512_kgm19004
A01 - first OPIM assignment

The purpose of this assignment is to get familiar with GitHub (website and desktop), making a repository, cloning it, and running a small code to make a box plot.

# Data used
A California Housing data set is used for this assignment. The data set contains the median income, house age, average rooms, average bedrooms, population, average occupation, latitude, longitude, and median house value.

The specific data used for my box plot is the house age.

# How to run the script
The script is run in the Visual Studio Code in python from GitHub Desktop.

The data is loaded, pandas is used for data manipulation, and matplotlib.pyplot is used to create the box plot. The data is returned as a pandas DataFrame and df is equal to the eight features and the target variable, which is the median house value. A quick data check shows the user what they are looking at.

The box plot is created by first designating the figure size (essentially 12 x 8 for this figure). The specific column chosen for the box plot is specified and a title and y-label is added. The figure is then saved to the figs file in A01_OPIM5512_kgm19004.

# Expected Output
The expected output is a saved box plot for the House Age. The box plot will indicate a maximum and minimum (shown by the top and bottom whisker), a median (green line), and the 25th and 75th percentile (top and bottom of the box).

