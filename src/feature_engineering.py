import sys
import os
sys.path.append(os.path.abspath("src"))
from data_cleaning import clean_data
def get_feature_engg_data():
 df = clean_data()
 df['Total_Marks']=df[['Math','Science','English']].sum(axis=1)

 df['Percentage']=((df['Total_Marks']/300)*100)
 df['Result']= df['Percentage'].apply(lambda x: 'Pass' if x>33 else 'Fail')

 df['Grade']=df['Percentage'].apply(lambda x: 
 'A+' if x>=90 else
 'A'  if x>=80 else
 'B+' if x>=70 else
 'B'  if x>=60 else
 'C+'  if x>=50 else
 'C'  if x>=40 else
 'D'  if x>=33 else
 'F'
    )
 return df
 

df = get_feature_engg_data()
df

