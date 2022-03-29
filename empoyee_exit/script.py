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

dete_survey_updated = dete_survey.drop(dete_survey.columns[28:49], axis=1)

dete_survey.columns

tafey_survey_updated = tafey_survey.drop(tafey_survey.columns[17:66], axis=1)
tafey_survey_updated.columns
