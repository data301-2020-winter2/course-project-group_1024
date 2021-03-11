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

    return df1

    # Method Chain 2 (Create new columns, drop others, and do processing)

