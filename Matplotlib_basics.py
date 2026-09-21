# matplotlib is mainly used for creating graphs and visualizing data

import matplotlib.pyplot as plt

# SIMPLE LINE PLOT
# plot() is used to create a line graph

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.show()


# LINE PLOT WITH LABELS

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.xlabel("X values")       # label of x-axis
plt.ylabel("Y values")       # label of y-axis
plt.title("My Line Graph")   # title of graph

plt.show()


# MARKERS
# marker shows the exact data points

plt.plot(x, y, marker="o")

plt.show()


# LINE STYLE

plt.plot(x, y, linestyle="--")

plt.show()


# BAR GRAPH
# bar() is used to create a bar graph

names = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()


# HORIZONTAL BAR GRAPH
# barh() creates a horizontal bar graph

plt.barh(names, marks)

plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()


# SCATTER PLOT
# scatter() shows the relationship between two variables

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")

plt.show()


# HISTOGRAM
# hist() shows the distribution of numerical data

marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")

plt.show()


# PIE CHART
# pie() creates a pie chart

subjects = ["Maths", "Science", "English", "Computer"]
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects)

plt.title("Subject Marks")

plt.show()


# ADD GRID
# grid() adds grid lines to the graph

plt.plot(x, y)

plt.grid()

plt.show()


# LEGEND
# legend() identifies different lines

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()

plt.show()


# TWO GRAPHS IN ONE FIGURE

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Two Lines")

plt.show()


# SUBPLOTS
# subplot() is used to create multiple graphs

plt.subplot(1, 2, 1)

plt.plot(x, y1)
plt.title("Line Graph")


plt.subplot(1, 2, 2)

plt.bar(x, y2)
plt.title("Bar Graph")

plt.show()


# SAVE GRAPH
# savefig() saves the graph as an image

plt.plot(x, y)

plt.savefig("my_graph.png")

plt.show()