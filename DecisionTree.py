import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('bankloan.csv')
pd.set_option('display.max_columns', None)
#print(df)
df['Experience'] = df['Experience'].abs()
X = df[["Age","Experience","Income","Family","CCAvg","Education","Mortgage",
        "Securities_Account","CD_Account","Online","CreditCard"]]
y = df["Personal_Loan"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

model = DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(X,y)
score = model.score(X,y)
print(score)

with open('bankloan.pkl', 'wb') as f:
    pkl.dump(model, f)

with open('Accuracy.pkl', 'wb') as f:
    pkl.dump(score,f)