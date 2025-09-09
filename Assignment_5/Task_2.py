import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("50_Startups.csv", delimiter=",")
print(df)

sns.heatmap(data=df.corr(numeric_only=True).round(2), annot=True)
plt.show()

plt.subplot(1, 2, 1)
plt.scatter(df['R&D Spend'],df['Profit'])
plt.xlabel('R&D Spend')
plt.ylabel('Profit')

plt.subplot(1, 2, 2)
plt.scatter(df['Marketing Spend'],df['Profit'])
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.show()

"""
Will use these variables for training and testing
"""
x = pd.DataFrame(df[['R&D Spend', 'Marketing Spend',]], columns = ['R&D Spend', 'Marketing Spend'])
y = df['Profit']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=5)

lm = LinearRegression()
lm.fit(x_train, y_train)

y_train_predict = lm.predict(x_train)
rmse = np.sqrt(mean_squared_error(y_train, y_train_predict))
r2 = r2_score(y_train, y_train_predict)
print("RMSE_Training",rmse)  #9358.583115148494
print("R2_Training",r2) # 0.9436198878593198

y_test_predict = lm.predict(x_test)
rmse_test = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test = r2_score(y_test, y_test_predict)
print("RMSE_Test",rmse_test) #7073.857168705303
print("R2_Test",r2_test) #0.9683604384024198



"""
Firstly by reading the file by using Pandas we got the variables 
inside the dataset. Then find the relation between the variables by using heatmap function.
From graph select the suitable variables, as in this R&D Spend with profit of 0.97 and Marketing Spend
with profit of 0.75 are having strong/positive correlation which could be 
good choice for predictors.

By using plt.scatter to know the relationship between each predictor and profit.Both predictors
show a linear relationship with profit but the relationship is stronger for R&D Spend due to less scatter
in the points than Marketing Spend. for both R&D Spend and Marketing Spend against profit, we got that

Then we train liner regression model with training data by using fit function.
Calculate the values of RMSE and R2 of training and testing data separately.
RMSE provides the prediction error means how much the predicted values deviate from the actual values. 
R2 gives the variance in profit with the help of predictors.
In this case RMSE_Training is 9358.58 i.e training data are far about $9358 from the actual profit.
RMSE_Test is 7073.86 i.e test data are far about $7074 from the actual profit.
R2 of this model explained that there are 94% of profit variance in training data and 96% in testing data.
"""
