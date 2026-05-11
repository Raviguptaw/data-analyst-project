#import necessary libraries
import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv('C:/Users/ravik/OneDrive/Desktop/data analyst project/indian employee dataset/Indian_Employee_Data.csv')
#print 
print(df.head())

#checking missing values
print('missing values in each column')
print(df.isnull().sum())

#checking salary = null and assign the null value with mean salary(avg salary)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# same with median(middle value) in ratings
df['Performance_Rating'].fillna(df['Performance_Rating'].median(),inplace=True)

#now replace infinite value with average value
df.replace([np.inf, -np.inf],np.nan,inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)

#replace negative salaries
df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(),df['Salary'])

salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

#remove rows where salary is too high or too low
df = df[(df['Salary'] >= lower_bound) & df['Salary'] <= upper_bound]

df.to_csv('cleaned_indian_employee_Data.csv',index=False)
print('data cleaning completed saved as cleaned_indian_employee_data.csv')

