import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(path)
          .loc[lambda x: ~x['Marital_Status'].str.contains("Unknown", na=False)]
          .loc[lambda x: ~x['Income_Category'].str.contains("Unknown", na=False)]
          .loc[lambda x: ~x['Education_Level'].str.contains("Unknown", na=False)]
          .reset_index()
          .drop('index', axis = 1)
     )


    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (df1
        .rename(columns = {'Card_Category':'Card Type','Customer_Age':'Age','Income_Category':'Income','Credit_Limit':'Credit Limit','Education_Level':'Education','Months_Inactive_12_mon':'Months Inactive','Total_Relationship_Count':'Relationship Count'})
        .drop(columns=['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Total_Ct_Chng_Q4_Q1','Total_Amt_Chng_Q4_Q1'])
          )
    
    return df2
