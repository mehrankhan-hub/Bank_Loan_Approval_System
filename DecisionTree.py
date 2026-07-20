import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('bankloan.csv')
pd.set_option('display.max_columns', None)
#print(df)
df['Experience'] = df['Experience'].abs()
X = df[["Age","Experience","Income","Family","CCAvg","Education","Mortgage",
        "Securities_Account","CD_Account","Online","CreditCard"]]
y = df["Personal_Loan"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X,y)
score = model.score(X,y)
print(score)

with open('bankloan.pkl', 'wb') as f:
    pkl.dump(model, f)

with open('Accuracy.pkl', 'wb') as f:
    pkl.dump(score,f)

print(df['Mortgage'].max())
print(df['Mortgage'].min())