#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def describeDf(df):
    print("Quantitative Data:")
    print(df.describe())
    print("\n")
    print("Qualitative Data:")
    print(df.describe(exclude=[np.number]))
    print("\n")
    print("Smoker/Non-Smoker Count:")
    print(df.Smoker.value_counts())

def EDAplots(df):
    #3 Lineplots for Chargs vs. Age/BMI/# of Children
    #1 Violin Plot for Smokers Charges vs. Non-Smokers Charges
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


def load_and_process(url_or_path_to_csv_file):

    df= (
    
        pd.read_csv(url_or_path_to_csv_file).rename(columns={"age": "Age","sex":"Sex","bmi":"BMI","children":"Children","smoker" : "Smoker", "region":"Region", "charges" : "Charges"})
        .drop(['Sex'], axis=1)
        .dropna()
        .sort_values(by=['Age'])
        .reset_index()
        .drop(['index'], axis=1)
        .assign(BMI_Class=lambda x: np.select([
        (x.BMI <=25),
        (x.BMI >25) & (x.BMI <= 30),
        (x.BMI >30) & (x.BMI <= 40),
        (x.BMI > 40) 
        ], ['Healthy', 'OverWeight', 'Obese', 'Extremely Obese']))
        
    )
    return df

##All Analysis Functions
def smokerVPlot(df):
    #Violin plot of Smoker/Non-Smoker charges
    sns.set_theme()
    plt.figure()
    fig=sns.violinplot(x='Charges', y="Smoker", data=df)
    fig.set_title("Distribution of Charges for Smokers and Non Smokers")
     ###Average Smoker/NonSmoker Charges
    print("Average Smoker Charges:")
    print(df[(df.Smoker=='yes')].Charges.mean())
    print("Average Non-Smoker Charges:")
    print(df[(df.Smoker=='no')].Charges.mean())

def boxPlotAge(df):
    #Box plot of charges per age group
    dfYoungOld=df
    dfYoungOld["Age Group"]=["Age<41" if x<41 else "Age>=41" for x in df['Age']]
    plt.figure()
    fig=sns.boxplot(x='Charges', y="Age Group", data=dfYoungOld, linewidth=2.5, palette='Set2')
    fig = sns.stripplot(x='Charges', y='Age Group', data=dfYoungOld, color="0.3", size=3)
    fig.set_title("Distribution of Charges for Ages Less than and Greater than or Equal to the Median Age")

def boxPlotBMIClass(df):
    #Box plot of charges per BMI class
    plt.figure()
    fig=sns.boxplot(x='Charges', y="BMI_Class", data=df, linewidth=2.5, palette='Set2', order=[ "Healthy", "OverWeight", "Obese", "Extremely Obese"])
    fig = sns.stripplot(x='Charges', y='BMI_Class', data=df, color="0.3", size=3, order=[ "Healthy", "OverWeight", "Obese", "Extremely Obese"])
    fig.set_title("Distribution of Charges for Each BMI Classification")
    

def boxPlotSmoker(df):
    #Box plot of smoker charges
    plt.figure()
    fig=sns.boxplot(x='Charges', y="Smoker", data=df, linewidth=2.5, palette='Set2')
    fig = sns.stripplot(x='Charges', y='Smoker', data=df, color="0.3", size=3)
    fig.set_title("Distribution of Charges for Smokers and Non-Smokers")

def boxPlotSmokerAge(df):
    ##Two boxplots with scatter plots overlain of Smokers Charges in two age groups
    plt.figure()
    fig=sns.boxplot(x='Charges', y="Smoker", data=df.loc[df["Age"]<41], linewidth=2.5, palette='Set2')
    fig = sns.stripplot(x='Charges', y='Smoker', data=df.loc[df["Age"]<41], color="0.3", size=3)
    fig.set_title("Distribution of Charges for Smokers and Non Smokers Younger than 41")

    
    plt.figure()
    fig=sns.boxplot(x='Charges', y="Smoker", data=df.loc[df["Age"]>=41], linewidth=2.5, palette='Set2')
    fig = sns.stripplot(x='Charges', y='Smoker', data=df.loc[df["Age"]>=41], color="0.3", size=3)
    fig.set_title("Distribution of Charges for Smokers and Non Smokers Older than 40")

def pieChartSmoker(df):
    ## Pie Chart of Smokers and Non-Smokers Contribution to Charges
    plt.figure()
    dfSmoker=df.loc[df["Smoker"]=="yes"]
    dfNonSmoker=df.loc[df["Smoker"]=="no"]
    labels = 'Smokers', 'Non-Smokers'
    sizes = [dfSmoker["Charges"].sum(),dfNonSmoker["Charges"].sum()]
    explode = (0.1,0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Smokers and Non-Smokers Contribution to Total Charges")
    plt.show()

def barSmokerBMI(df):
    #Bar plot of smokers and non-smokers in each BMI class
    plt.figure()
    fig = sns.countplot(x="BMI_Class", hue="Smoker", data=df, order=[ "Healthy", "OverWeight", "Obese", "Extremely Obese"])
    fig.set_title("Smokers and Non Smokers in Each BMI Class")

def barAgeBMI(df):
    #Bar plot of age groups in each BMI class
    plt.figure()
    dfYoungOld=df
    dfYoungOld["Age Group"]=["18<=age<30" if x<30 else "30<=Age<41" if x>=30 and x<41 else "41<=Age<52" if x>=41 and x<52 else "Age>52" for x in df['Age']]
    fig = sns.countplot(x="BMI_Class", hue="Age Group", data=df, order=[ "Healthy", "OverWeight", "Obese", "Extremely Obese"])
    fig.set_title("Age Groups in Each BMI Class")
    
