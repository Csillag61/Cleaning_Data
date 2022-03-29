import pandas as pd
import numpy as np

dete_survey = pd.read_csv('dete_survey.csv')
tafe_survey = pd.read_csv('tafe_survey.csv')

dete_survey.head()
dete_survey.info()
#dete_survay.value_counts()
dete_survey.isnull()
