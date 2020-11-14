#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def EDA(df):
    print(df.describe())
    print(df.describe(exclude=[np.number]))
    print(df.Smoker.value_counts())
   
    plt.figure()
    fig2=sns.lineplot(data=df, x="BMI", y="Charges")
    fig2.set_title("Total Charges vs. BMI")
    
    plt.figure()
    fig3=sns.lineplot(data=df, x="Age", y="Charges")
    fig3.set_title("Total Charges vs. Age")

    plt.figure()
    fig3=sns.lineplot(data=df, x="Children", y="Charges")
    fig3.set_title("Total Charges vs. Number of Children")

    plt.figure()
    fig=sns.violinplot(x='Charges', y="Smoker", data=df)
    fig.set_title("Distribution of Charges for Smokers and Non Smokers")

    print("From df.describe() we can see the ranges of age, BMI and number of children. We can also see that the average BMI is relatively low, as well as the average children being quite low at slightly above 1. \n From this EDA we can tell how each of the four attributes relates to total Charges accrued. Firstly the plot of BMI and charges shows a small increase along the x/y slope, but there is an extensive amount of variation. Secondly we see the expected slope on the Age vs Charges plot, but it is not too steep and has a lot of variation. Number of Children vs Charges actually shows a parabola, where charges start to go down on average after the third child but there is also the most amount of deviation of all the plots. Finally the Smokers vs Non-Smokers chart shows a stark difference in grouping and average cost between Smokers and non-Smokers. ")

    return

def load_and_process(url_or_path_to_csv_file):

    df= (
    
        pd.read_csv(url_or_path_to_csv_file).rename(columns={"age": "Age","sex":"Sex","bmi":"BMI","children":"Children","smoker" : "Smoker", "region":"Region", "charges" : "Charges"})
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



