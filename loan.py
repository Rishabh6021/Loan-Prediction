import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv("train_u6lujuX_CVtuZ9i.csv")
test=pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")
print(train['Loan_Status'].value_counts())

#print(train.isnull().sum())    
train['Gender']=train['Gender'].fillna(train['Gender'].mode()[0])
print(train.isnull().sum())