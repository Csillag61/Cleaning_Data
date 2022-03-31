import pandas as pd
import numpy as np

dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')

dete_survey.head()
dete_survey.info()
#dete_survay.value_counts()
dete_survey.isnull()

#The dete_survey dataframe contains 'Not Stated' values that indicate values are missing, but they aren't represented as NaN.
# Both the dete_survey and tafe_survey dataframes contain many columns that we don't need to complete our analysis.
# Each dataframe contains many of the same columns, but the column names are different.
# There are multiple columns/answers that indicate an employee resigned because they were dissatisfied.

# To start, we'll handle the first two issues. Recall that we can use the pd.read_csv() function to specify values that should be represented as NaN. We'll use this function to fix the missing values first. Then, we'll drop columns we know we don't need for our analysis.

dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')

tafe_survey = pd.read_csv('tafe_survey.csv', na_values='Not Stated')
tafe_survey.head()

dete_survey.columns

#standardize the column names
dete_survey_updated=dete_survey.drop(dete_survey.columns[28:49], axis=1)
dete_survey_updated.columns = dete_survey_updated.columns.str.lower().str.strip().str.replace(' ', '_')

dete_survey_updated.columns

tafey_survey_updated = tafey_survey.drop( tafey_survey.columns[17:66], axis=1)
tafey_survey_updated.columns

mapping={'Record ID': 'id', 
            'CESSATION YEAR': 'cease_date', 
            'Reason for ceasing employment': 'separationtype', 
            'Gender. What is your Gender?': 'gender', 
            'CurrentAge. Current Age': 'age',
            'Employment Type. Employment Type': 'employment_status',
            'Classification. Classification': 'position',
            'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service',
            'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'}

tafe_survey_updated = tafe_survey_updated.rename(mapping, axis= 1)
tafe_survey_updated.columns    

#Are employees who have only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been at the job longer?

dete_survey_updated['separationtype'].value_counts()
# Age Retirement                          285
# Resignation-Other reasons               150
# Resignation-Other employer               91
# Resignation-Move overseas/interstate     70
# Voluntary Early Retirement (VER)         67
# Ill Health Retirement                    61
# Other                                    49
# Contract Expired                         34
# Termination                              15
# Name: separationtype, dtype: int64

tafe_survey_updated['separationtype'].value_counts()

# Resignation                 340
# Contract Expired            127
# Retrenchment/ Redundancy    104
# Retirement                   82
# Transfer                     25
# Termination                  23
# Name: separationtype, dtype: int64

# Update all separation types containing the word "resignation" to 'Resignation'
dete_survey_updated['separationtype'] = dete_survey_updated['separationtype'].str.split('-').str[0]

# Check the values in the separationtype column were updated correctly
dete_survey_updated['separationtype'].value_counts()

# Resignation                         311
# Age Retirement                      285
# Voluntary Early Retirement (VER)     67
# Ill Health Retirement                61
# Other                                49
# Contract Expired                     34
# Termination                          15
# Name: separationtype, dtype: int64

tafe_resignations = tafe_survey_updated[tafe_survey_updated['separationtype'] == 'Resignation'].copy()
dete_resignations = dete_survey_updated[dete_survey_updated['separationtype'] == 'Resignation'].copy()

# Since the cease_date is the last year of the person's employment and the dete_start_date is the person's first year of employment, it wouldn't make sense to have years after the current date. Given that most people in this field start working in their 20s, it's also unlikely that the dete_start_date was before the year 1940.

dete_resignations['cease_date'].value_counts()
# 2012       126
# 2013        74
# 01/2014     22
# 12/2013     17
# 06/2013     14
# 09/2013     11
# 07/2013      9
# 11/2013      9
# 10/2013      6
# 08/2013      4
# 05/2012      2
# 05/2013      2
# 07/2012      1
# 2010         1
# 09/2010      1
# 07/2006      1
# Name: cease_date, dtype: int64

# Extract the years and convert them to a float type

dete_resignations['cease_date']=dete_resignations['cease_date'].str.split('/').str[-1]
dete_resignations['cease_date'] = dete_resignations['cease_date'].astype("float")

# Check the values again and look for outliers
dete_resignations['cease_date'].value_counts()
# Check the unique values and look for outliers
dete_resignations['dete_start_date'].value_counts().sort_index(ascending=True)

# Check the unique values and look for outliers
tafe_resignations['cease_date'].value_counts().sort_values()
dete_resignations['institute_service'] = dete_resignations['cease_date'] -
dete_resignations['dete_start_date']

tafe_resignations['Contributing Factors. Dissatisfaction'].value_counts()

tafe_resignations['Contributing Factors. Job Dissatisfaction'].value_counts()

