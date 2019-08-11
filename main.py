import pandas as pd
import numpy as np

# define `df1`
df1 = pd.ExcelFile("data/test1.xlsx").parse("Sheet1")
# print(df1.head())

# define `df2`
df2 = pd.ExcelFile("data/test2.xlsx").parse("Sheet1")
# print(df2.head())

# define `df3`
df3 = df2
df3.insert(1, column= "quality", value= np.nan)     # position 1: 2nd column
df3.insert(2, column= "secure", value= np.nan)      # position 2: 3rd column

# define 'App_Names' list for the `for` loop
list_app_names = df1['App_Names'].tolist()

"""
Description
===========
for loop introduced to apply the rules in the entire series ['App1', ......'App13'] 

For single `App1`:
------------------
df3.loc[df3.App_Names == 'App1', ['quality', 'secure']] = [df1.iloc[0,1], df1.iloc[0,2]]
"""
for i in range(len(list_app_names)):
    df3.loc[df3.App_Names == list_app_names[i], ['quality', 'secure']] = [df1.iloc[i,1], df1.iloc[i,2]]

df3.to_excel("output.xlsx", index= False)



