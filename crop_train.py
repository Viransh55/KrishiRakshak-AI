import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("crop_data.csv")

X = data[['Moisture','Temperature','Humidity']]
y = data['Crop']

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

joblib.dump(model,'crop_model.pkl')

prediction = model.predict([[70,22,75]])

print("Recommended Crop:",prediction[0])

print("Crop Model Saved Successfully!")