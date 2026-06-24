import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("irrigation.csv")

X = data[['Moisture','Temperature','Humidity']]
y = data['Irrigation']

model = DecisionTreeClassifier()

model.fit(X,y)

joblib.dump(model,'irrigation_model.pkl')

print("Irrigation Model Saved Successfully!")