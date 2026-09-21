# seaborn is mainly used for statistical data visualization
# seaborn works very well with pandas DataFrame

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# CREATE DATAFRAME

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [80, 90, 70, 85, 95]
}

df = pd.DataFrame(data)

print(df)


# LINE PLOT
# sns.lineplot() creates a line graph

sns.lineplot(data=df, x="Age", y="Marks")

plt.show()


# BAR PLOT
# sns.barplot() creates a statistical bar graph

sns.barplot(data=df, x="Name", y="Marks")

plt.show()


# SCATTER PLOT
# sns.scatterplot() shows relationship between two variables

sns.scatterplot(data=df, x="Age", y="Marks")

plt.show()


# HISTOGRAM
# sns.histplot() shows distribution of data

sns.histplot(data=df, x="Marks")

plt.show()


# COUNT PLOT
# countplot() counts how many times each category occurs

data = {
    "City": ["Bhopal", "Delhi", "Bhopal", "Indore", "Delhi", "Bhopal"]
}

df2 = pd.DataFrame(data)

sns.countplot(data=df2, x="City")

plt.show()


# BOX PLOT
# boxplot() shows distribution and possible outliers

sns.boxplot(data=df, y="Marks")

plt.show()


# VIOLIN PLOT
# violinplot() shows distribution of data

sns.violinplot(data=df, y="Marks")

plt.show()


# PAIR PLOT
# pairplot() creates relationships between multiple numerical columns

data = {
    "Maths": [80, 70, 90, 60, 85],
    "Science": [85, 75, 95, 65, 80],
    "English": [70, 80, 85, 75, 90]
}

df3 = pd.DataFrame(data)

sns.pairplot(df3)

plt.show()


# HEATMAP
# heatmap() is commonly used to show correlation

correlation = df3.corr()

sns.heatmap(correlation)

plt.show()


# HEATMAP WITH VALUES
# annot=True displays values inside the heatmap

sns.heatmap(correlation, annot=True)

plt.show()


# COLOR PALETTE

sns.barplot(
    data=df,
    x="Name",
    y="Marks",
    palette="viridis"
)

plt.show()


# ADD TITLE

sns.scatterplot(data=df, x="Age", y="Marks")

plt.title("Age vs Marks")

plt.show()


# SET SEABORN STYLE

sns.set_style("whitegrid")

sns.scatterplot(data=df, x="Age", y="Marks")

plt.show()