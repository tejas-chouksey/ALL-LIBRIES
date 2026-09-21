# pandas is used mainly for data analysis and data manipulation
# pandas is mainly used to work with tables, rows and columns

import pandas as pd

# SERIES
# Series is a single column of data
marks = pd.Series([80, 70, 90, 60])
print(marks)


# DATAFRAME
# DataFrame is a table containing rows and columns
data = {
    "Name": ["Rahul", "Aman", "Priya", "Rohit"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 90, 75, 85]
}
df = pd.DataFrame(data)
print(df)

# HEAD
# head() shows first 5 rows by default
print(df.head())
# user can give number of rows
print(df.head(2))

# TAIL
# tail() shows last 5 rows by default
print(df.tail())
# user can give number of rows
print(df.tail(2))

# SHAPE
# shape tells number of rows and columns
print(df.shape)

# COLUMNS
# columns shows all column names
print(df.columns)

# INDEX
# index shows row indexes
print(df.index)

# INFO
# info() gives information about DataFrame
df.info()

# DESCRIBE
# describe() gives statistical information about numerical columns
print(df.describe())

# ACCESS ONE COLUMN
# use column name to access one column
print(df["Name"])
print(df["Marks"])

# ACCESS MULTIPLE COLUMNS
# use list of column names to access multiple columns
print(df[["Name", "Marks"]])

# ACCESS ROW USING ILOC
# iloc is used to access rows using position
print(df.iloc[0])       # first row
print(df.iloc[1])       # second row

# ACCESS SPECIFIC VALUE USING ILOC
# iloc[row, column]
print(df.iloc[0, 1])    # first row, second column
print(df.iloc[2, 2])    # third row, third column

# ACCESS ROW USING LOC
# loc is used to access rows using index label
print(df.loc[0])
print(df.loc[2])

# ADD NEW COLUMN
# create a new column by using a new column name
df["Pass"] = True
print(df)

# ADD COLUMN USING CONDITION
df["Passed"] = df["Marks"] >= 40
print(df)

# UPDATE COLUMN
df["Marks"] = df["Marks"] + 5
print(df)

# DELETE COLUMN
# drop() is used to remove a column
df = df.drop("Pass", axis=1)
print(df)

# FILTERING
# get rows where Marks are greater than 80
result = df[df["Marks"] > 80]
print(result)

# FILTERING WITH TWO CONDITIONS
# & means AND
result = df[(df["Age"] > 20) & (df["Marks"] > 80)]
print(result)

# FILTERING WITH OR
# | means OR
result = df[(df["Age"] > 20) | (df["Marks"] > 80)]
print(result)

# SORTING
# sort_values() is used to sort data
print(df.sort_values("Marks"))

# SORTING IN DESCENDING ORDER
print(df.sort_values("Marks", ascending=False))

# SUM
# sum() gives total of values
print(df["Marks"].sum())

# MEAN
# mean() gives average
print(df["Marks"].mean())

# MAX
# max() gives maximum value
print(df["Marks"].max())

# MIN
# min() gives minimum value
print(df["Marks"].min())

# MEDIAN
# median() gives middle value
print(df["Marks"].median())

# COUNT
# count() counts non-empty values
print(df["Marks"].count())

# UNIQUE
# unique() gives unique values
print(df["Age"].unique())

# NUNIQUE
# nunique() gives number of unique values
print(df["Age"].nunique())

# VALUE COUNTS
# value_counts() counts how many times each value occurs
data2 = {
    "City": ["Bhopal", "Indore", "Bhopal", "Delhi", "Indore", "Bhopal"]
}
df2 = pd.DataFrame(data2)
print(df2["City"].value_counts())

# CHECK MISSING VALUES
# isnull() checks whether values are missing
print(df.isnull())

# COUNT MISSING VALUES
# isnull().sum() counts missing values in each column
print(df.isnull().sum())

# CREATE DATA WITH MISSING VALUE
data3 = {
    "Name": ["Rahul", "Aman", "Priya", "Rohit"],
    "Age": [20, None, 19, 22],
    "Marks": [80, 90, None, 85]
}
df3 = pd.DataFrame(data3)
print(df3)

# FILL MISSING VALUES
# fillna() is used to fill missing values
df3["Age"] = df3["Age"].fillna(df3["Age"].mean())
print(df3)

# DROP MISSING VALUES
# dropna() removes rows containing missing values
df3 = df3.dropna()
print(df3)

# RENAME COLUMN
# rename() is used to change column names
df = df.rename(columns={"Marks": "Score"})
print(df)

# CHANGE COLUMN NAME BACK
df = df.rename(columns={"Score": "Marks"})
print(df)

# ADD ROW
# loc can be used to add a new row
df.loc[len(df)] = ["Neha", 20, 95, True]
print(df)

# REMOVE ROW
# drop() can be used to remove a row
df = df.drop(0)
print(df)

# RESET INDEX
# reset_index() creates a new index after deleting rows
df = df.reset_index(drop=True)
print(df)

# READ CSV FILE
# read_csv() is used to read a CSV file

# df = pd.read_csv("students.csv")

# print(df)


# SAVE DATAFRAME TO CSV
# to_csv() saves DataFrame as a CSV file

# df.to_csv("students_new.csv", index=False)


# READ EXCEL FILE
# read_excel() is used to read Excel files

# df = pd.read_excel("students.xlsx")

# print(df)


# SAVE DATAFRAME TO EXCEL

# df.to_excel("students_new.xlsx", index=False)


# GROUPBY
# groupby() is used to group data based on a column

data4 = {
    "Department": ["IT", "IT", "HR", "HR", "Sales"],
    "Salary": [30000, 40000, 25000, 35000, 45000]
}
df4 = pd.DataFrame(data4)
print(df4.groupby("Department")["Salary"].mean())

# GROUPBY SUM
print(df4.groupby("Department")["Salary"].sum())

# APPLY OPERATION ON COLUMN
# calculate total marks after adding 10
df["Marks"] = df["Marks"] + 10
print(df)

# STRING OPERATION
# str.upper() converts text to uppercase
df["Name"] = df["Name"].str.upper()
print(df)

# STRING OPERATION
# str.lower() converts text to lowercase
df["Name"] = df["Name"].str.lower()
print(df)

# STRING REPLACE
# str.replace() replaces text
df["Name"] = df["Name"].str.replace("rahul", "rohan")
print(df)

# QUERY
# query() can be used for filtering data
result = df.query("Marks > 80")
print(result)

# COPY
# copy() creates a separate copy of DataFrame
df_copy = df.copy()
print(df_copy)

# CORRELATION
# corr() shows correlation between numerical columns
data5 = {
    "Maths": [80, 70, 90, 60, 85],
    "Science": [85, 75, 95, 65, 80],
    "English": [70, 80, 85, 75, 90]
}
df5 = pd.DataFrame(data5)
print(df5.corr())

# COVARIANCE
# cov() shows covariance between numerical columns
print(df5.cov())

# ROW-WISE SUM
# axis=1 means calculate across columns for each row
print(df5.sum(axis=1))

# COLUMN-WISE SUM
# axis=0 means calculate down each column
print(df5.sum(axis=0))