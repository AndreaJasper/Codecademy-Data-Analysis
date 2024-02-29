import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())

# cleans birth_year by filling in missing data
census['birth_year'] = census['birth_year'].replace('missing', '1967')
# print(census['birth_year'].unique())

# convert birth_year from str to int
census['birth_year'] = census['birth_year'].astype('int')

# get average birth year
print(census['birth_year'].mean())

# set order to higher_tax
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)
print(census['higher_tax'].unique())

# find median sentiment of respondents
census['higher_tax'] = census['higher_tax'].cat.codes
print(census['higher_tax'].median())

# OHE marital_status to create binary vars
census_1 = pd.get_dummies(census, columns=['marital_status'])
print(census_1.head())

# encode marital_status
census['marital_codes'] = pd.Categorical(census['marital_status'], ['single', 'divorced', 'married', 'widowed'], ordered=False)

census['marital_codes'] = census['marital_codes'].cat.codes

print(census.head())

# group by age
current_year = 2024
census['age'] = current_year - census['birth_year']
census['age_group'] = pd.cut(census['age'], bins=range(0,101,5), labels=[f"{i}-{i+4}" for i in range(0,100,5)], right=False)

census['age_group_encoded'] = census['age_group'].cat.codes
print(census.head())
