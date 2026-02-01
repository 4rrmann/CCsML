import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# load dataset
df = pd.read_csv("placement.csv")

# features & target
X = df[["cgpa", "iq"]]
y = df["placement"]

# ML pipeline
model = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),  # fill NaNs with mean
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

# train
model.fit(X, y)

# save pipeline (model + preprocessing)
pickle.dump(model, open("placement_model.pkl", "wb"))

print("Model trained & saved!")