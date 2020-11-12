#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):

    df= (
    
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"age": "Age", "sex": "Sex", "bmi": "BMI", "children":"Children", "smoker" : "Smoker", "region":"Region", "charges" : "Charges"})
        .drop(['Sex'], axis=1)
        .dropna()
        .sort_values(by=['Age'])
        .reset_index()
        .drop(['index'], axis=1)
        .assign(BMI_Class=lambda x: np.select([
        (x.BMI <25),
        (x.BMI >25) & (x.BMI < 30),
        (x.BMI >30) & (x.BMI < 40),
        (x.BMI > 40) 
        ], ['Healthy', 'OverWeight', 'Obese', 'Extremely Obese']))
    
    )
    
    return df


