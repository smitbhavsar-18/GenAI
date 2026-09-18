#Task 1 : Pandas Series Basics

import pandas as pd

marks = [78, 85 , 90, 66, 72]

marks_series = pd.Series(marks)

print("Pandas Series:", marks_series)

print("Series Values:", marks_series.values)
print("Series Index:", marks_series.index)
print("Series Data Type:", marks_series.dtype)

print("first element of series:", marks_series[0])
print("last two elements of series:", marks_series[-2:])

#task 2: Math Operations on Pandas Series

print("Add 5 Grace Marks to each student:", marks_series + 5)
print("Subtract 2 Marks from each student:", marks_series - 2)
print("Multiply each student's marks by 1.05:", marks_series * 1.05)
print("Divide each student's marks by 2:", marks_series / 2)

#Task 3: Python Functions on Pandas Series

print("Maximum Marks:", marks_series.max())
print("Minimum Marks:", marks_series.min())
print("sum of all Marks:", marks_series.sum())
print("mean of all Marks:", marks_series.mean())
print("lambda function to check whether marks are greater than or equal to 70:", marks_series.apply(lambda x: x >= 70))
print("count how many students passed the exam:", marks_series[marks_series >= 70].count())

#Task 4 : Create a Pandas DataFrame

students = {
    'Name' : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85 , 90, 66, 72],
    'Subject' : ["Math", "Math", "Science", "Science", "Math"]
}

students_df = pd.DataFrame(students)
print("Pandas DataFrame:\n", students_df)

print("Print first three rows of DataFrame:\n", students_df.head(3))
print("Print last two rows of DataFrame:\n", students_df.tail(2))
print("DataFrame shape:", students_df.shape)
print("DataFrame columns:", students_df.columns)

#Task 5: Important DataFrame Functions

print("DataFrame Info:\n", students_df.info())
print("DataFrame Describe:\n", students_df.describe())
print("DataFrame head:\n", students_df.head())
print("DataFrame tail:\n", students_df.tail())

students_df_sorted = students_df.sort_values(by='Marks', ascending=False)
print("DataFrame sorted by Marks in descending order:\n", students_df_sorted)
students_df_reset = students_df_sorted.reset_index(drop=True)
print("DataFrame after resetting index:\n", students_df_reset)

#Task 6: Filtering & Conditionals Selection in DataFrame

print("Students who scored more than 75 marks:\n", students_df[students_df['Marks'] > 75])
print("students belonging to Math subject:\n", students_df[students_df['Subject'] == 'Math'])
print("student who scored more than average marks:\n", students_df[students_df['Marks'] > students_df['Marks'].mean()])
print("students who failed the exam (marks < 70):\n", students_df[students_df['Marks'] < 70])

#Task 7: Grouping & Basic Analysis in DataFrame

print("Group by Subject and calculate average marks:\n", students_df.groupby('Subject')['Marks'].mean())
print("Count number of students in each subject:\n", students_df.groupby('Subject')['Subject'].count())
print("Maximum marks in each subject:\n", students_df.groupby('Subject')['Marks'].max())

#Task 8: Pandas Plotting

students_df.plot(kind='bar', x='Name', y='Marks')

students_df['Marks'].plot(kind='line')

students_df['Marks'].plot(kind='hist')

#Task 9 : Mini Use Case: Sales Data Analysis

sales = {
    'Day' : ["Mon", "Tue", "Wed", "Thu", "Fri"],
    'Revenue' : [1200, 1500, 900, 2000, 1800],
}

sales_df = pd.DataFrame(sales)

print("Total Revenue:", sales_df['Revenue'].sum())
print("Average Daily Revenue:", sales_df['Revenue'].mean())
print("Day with Maximum Revenue:", sales_df.loc[sales_df['Revenue'].idxmax()]['Day'])
print("Day where revenue > average revenue:", sales_df[sales_df['Revenue'] > sales_df['Revenue'].mean()])

sales_df.plot(kind='bar', x='Day', y='Revenue')