## Important Libraries as requirements
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
## Machine Learning Libraries that I have Used for building the model, training, testing and evaluating the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# load the tips dataset from seaborn's github
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# quick look at the data before doing anything else
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())  # just making sure there's nothing missing

# need to convert categorical columns (sex, smoker, day, time) into numbers
# using one-hot encoding, dropping first category to avoid dummy trap
df_encoded = pd.get_dummies(df, drop_first=True)
print(df_encoded.head())

# tip is what we're trying to predict, everything else is a feature
X = df_encoded.drop("tip", axis=1)
y = df_encoded["tip"]

# 80/20 split, random_state so results are reproducible
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# generate predictions on the test set
predictions = model.predict(X_test)

# check how well the model actually performed
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("RMSE:", rmse)
print("R2:", r2)

# let's see which features matter the most
coefficients = pd.DataFrame({
    "Variable": X.columns,
    "Coefficient": model.coef_
})
coefficients["Absolute"] = coefficients["Coefficient"].abs()
coefficients = coefficients.sort_values("Absolute", ascending=False)
print(coefficients)

# plotting the coefficients to visualize their impact
plt.figure(figsize=(10, 6))
sns.barplot(data=coefficients, x="Coefficient", y="Variable")
plt.title("Influence of Variables on Tip Amount")
plt.tight_layout()
plt.savefig("visualization.png")
plt.show()

# Thank you very much, I have used Pycharm Python for this test. I am look forward to hearing from you if I am successful
# Charles Daniel Apollo
# charlesdanieldoka@gmail.com