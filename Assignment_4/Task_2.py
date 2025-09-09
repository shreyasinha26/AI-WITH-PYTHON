import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("weight-height.csv")
x = data["Height"].values
y = data["Weight"].values
xp = x.reshape(-1, 1)
yp = y.reshape(-1, 1)

model = LinearRegression()
model.fit(xp, yp)

y_sklearn = model.predict(xp)

plt.scatter(x,y, color='blue', label='Data points')
plt.plot(x, y_sklearn, color='red', label='Linear Regression')
plt.xlabel("x: Height")
plt.ylabel("y: Weight")
plt.title("Linear Rgression: ")
plt.show()

RMSE = np.sqrt(mean_squared_error(y, y_sklearn))
R2 = r2_score(y, y_sklearn)
print(f"RMSE: {RMSE:}") # RMSE: 12.218571272826035
print(f"R2: {R2:}") # R2: 0.8551742120609958


# 6. Quality of regression: Output shows the blue dots as an actual data points of a given sample
# Red line is the regression line.
#R2 is close to 1 which depicts that change in weight depends on height.
#Values that RMSE is low means prediction is very close to actual values.
#This model provides the weight more precisely.
