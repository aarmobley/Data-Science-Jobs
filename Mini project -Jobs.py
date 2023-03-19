# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import packages being used
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
Jobs = pd.read_csv( r"C:\Users\Aaron Mobley\Downloads\gsearch_jobs.csv")

#data wrangling -Drop columns 
Jobs2 = Jobs.drop([ 'via', 'extensions', 'thumbnail', 'job_id', 'posted_at', 'description', 
                   'description_tokens', 'search_location'], axis=1)
Jobs3 = Jobs2.drop('commute_time', axis = 1)

#What is the most searched for term?
Jobs3['search_term'].describe()
#Data analyst is the top searched for term and the only searched for term

#Are there more jobs remote or on location?
Jobs3['location'].describe()
#Anywhere is the top option- Work from home


# Drop all NA values

Jobs4 = Jobs3.dropna(subset=['salary_standardized'])

#Drop more unnessecary columns
Jobs5 = Jobs4.drop(['salary_hourly', 'work_from_home', 'salary_yearly', 'salary_min', 'salary_max'], axis=1)

Jobs5['salary_standardized'].describe()

Jobs5.to_csv(r'C:\Users\Aaron Mobley\Desktop\Python\Jobs4.csv')

#Sort Jobs with the highest paying salaries at the top

Jobs6 = Jobs5.sort_values('salary_standardized', ascending=False)

Jobs6.to_csv(r'C:\Users\Aaron Mobley\Desktop\Python\Jobs6.csv')

#Data Analyst for Ecommerce and Marketing Agency at Upwork is the highest paying job


