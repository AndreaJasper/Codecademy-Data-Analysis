# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe(include='all'))

# Calculate mean
print('Mean: ' + str(round(students.math_grade.mean(), 1)))

# Calculate median
print('Median: ' + str(students.math_grade.median()))

# Calculate mode
print('Mode: ' + str(students.math_grade.mode()[0]))

# Calculate range
math_range = students.math_grade.max() - students.math_grade.min()
print('Range: ' + str(math_range))

# Calculate standard deviation
print('Standard Deviation: ' + str(round(students.math_grade.std(), 1)))

# Calculate MAD
print('MAD: ' + str(round(students.math_grade.mad(), 1)))

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print('Mom Jobs: ' + str(students['Mjob'].value_counts()))

# Calculate proportion of students with mothers in each job category
print('Mom Jobs Proportion: ' + str(students['Mjob'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'))

# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
# students.Mjob.value_counts().plot.pie()
# plt.show()

# Further exploration
# # Calculate number of students with addresses in each category
print('Address: ' + str(students['address'].value_counts()))

# Calculate proportion of students in each category
print('Address Proportion: ' + str(students['address'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'))

# Create bar chart of address
sns.countplot(x='address', data=students)
plt.show()
plt.clf()

# Calculate number of students with fathers in each job category
print('Father Jobs: ' + str(students['Fjob'].value_counts()))

# Calculate proportion of students with fathers in each job category
print('Father Jobs Proportion: ' + str(students['Fjob'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'))

# Create bar chart of Fjob
sns.countplot(x='Fjob', data=students)
plt.show()
plt.clf()

# Calculate the central tendency and spread for absences
print('Absence Mean: ' + str(round(students.absences.mean(), 1)))
print('Absence Median: ' + str(students.absences.median()))
print('Absence Mode: ' + str(students.absences.mode()[0]))

sns.histplot(x='absences', data=students)
plt.show()
plt.clf()