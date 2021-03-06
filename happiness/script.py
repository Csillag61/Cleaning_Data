# Remove any rows that have missing values.
# Remove any columns that have missing values.
# Fill the missing values with some other value.
# Leave the missing values as is.
import pandas as pd
import seaborn as sns

happiness2015 = pd.read_csv('wh_2015.csv')
happiness2016 = pd.read_csv('wh_2016.csv')
happiness2017 = pd.read_csv('wh_2017.csv')

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape
shape_2017 = happiness2017.shape

missing_2015 = happiness2015.isnull().sum()
missing_2017 = happiness2017.isnull().sum()

happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2015.columns = happiness2015.columns.str.replace('(', '').str.replace(')', '').str.strip().str.upper()
happiness2016.columns = happiness2016.columns.str.replace('(', '').str.replace(')', '').str.strip().str.upper()

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
missing = combined.isnull().sum()

#heatmap of missing data
combined_updated = combined.set_index('YEAR')
sns.heatmap(combined_updated.isnull(), cbar=False)
regions_2017 = combined[combined['YEAR'] == 2017]['REGION']
missing = regions_2017.isnull().sum() #164
regions= pd.DataFrame()
regions['COUNTRY']= combined['COUNTRY']
regions['REGION']=combined['REGION']
regions=pd.concat([regions['COUNTRY'], regions['REGION']], axis=1)

combined = pd.merge(left=combined, right=regions, on='COUNTRY', how='left')
combined = combined.drop('REGION_x', axis=1)
missing = combined.isnull().sum()

combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
print(combined[dups])

combined[combined['COUNTRY'] == 'SOMALILAND REGION']
combined['COUNTRY'] = combined['COUNTRY'].str.upper()
combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])
combined.isnull().sum()
mapping = {'REGION__y': 'REGION'}
combined.rename(mapping, inplace=True)
combined.isnull().sum()

columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH', 'WHISKER LOW']

combined=combined.drop(columns_to_drop, axis=1)
missing=combined.isnull().sum()
combined.notnull().sum().sort_values()

#set the thresh parameter equal to 159 in the df.dropna() method to drop them.

combined=combined.dropna(axis=1, thresh=159)
missing=combined.isnull().sum()

sorted = combined.set_index('REGION').sort_values(['REGION', 'HAPPINESS SCORE'])
sns.heatmap(sorted.isnull(), cbar=False)

happiness_mean = combined['HAPPINESS SCORE'].mean()
print(happiness_mean)
combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna( happiness_mean )
print(combined['HAPPINESS SCORE UPDATED'].mean())
combined = combined.dropna()
missing = combined.isnull().sum()