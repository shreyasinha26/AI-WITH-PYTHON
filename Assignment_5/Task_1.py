import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes(as_frame=True)
print(data.DESCR)
df = data.frame
print(df.head())

plt.hist(df['target'],25)
plt.xlabel('target')
plt.show()

sns.heatmap(data=df.corr().round(2), annot=True)
plt.show()

plt.subplot(1, 2, 1)
plt.scatter(df['bmi'], df['target'])
plt.xlabel('bmi')
plt.ylabel('target')
plt.subplot(1, 2, 2)
plt.scatter(df['s5'], df['target'])
plt.xlabel('s5')
plt.ylabel('target')
plt.show()


X = pd.DataFrame(df[['bmi','s5']], columns = ['bmi','s5'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)

lm = LinearRegression()
lm.fit(X_train, y_train)

y_train_predict = lm.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)
print("RMSE_Training",rmse) # 56.560890965481114
print("R2_Training",r2) # 0.4507519215172524

y_test_predict = lm.predict(X_test)
rmse_test = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test = r2_score(y_test, y_test_predict)
print("RMSE_Test",rmse_test) # 57.1759740950605
print("R2_Test",r2_test) #0.4815610845742896

"""
bmi and s5 are most predictive for diabetes progression in this dataset.
I would like to add next variable as bp because it has strong correlation 
with target 0.44
"""
#After Adding bp as variable:
X1 = pd.DataFrame(df[['bmi','s5', 'bp']], columns = ['bmi','s5','bp'])
#y = df['target']
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y, test_size = 0.2, random_state=5)

lm1 = LinearRegression()
lm1.fit(X_train1, y_train1)

y_train_predict1 = lm1.predict(X_train1)
rmse_train1 = (np.sqrt(mean_squared_error(y_train1, y_train_predict1)))
r2_train1 = r2_score(y_train1, y_train_predict1)
print("RMSE_Training1",rmse_train1) #55.32610611166316
print("R2_Training1",r2_train1) #0.47447150038132146

y_test_predict1 = lm1.predict(X_test1)
rmse_test1 = (np.sqrt(mean_squared_error(y_test1, y_test_predict1)))
r2_test1 = r2_score(y_test1, y_test_predict1)
print("RMSE_Test1",rmse_test1) # 56.6256100515053
print("R2_Test1",r2_test1) #0.4914938186648421

"""
Effect of adding the variable bp  with bmi and s5 is that R2 of training set has improved from 
0.45 to 0.47 and RMSE(Error) has reduced from 56.5 to 55.3
similarly, R2 of test set has improved from 0.48 to 0.49 and RMSE(Error) has 
reduced from 57.1 to 56.6 means improvement is moderate.

"""
# By adding reaming variables from the dataframe.

X_rem = df.drop(columns=['target'])
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_rem, y, test_size = 0.2, random_state=5)

lm2 = LinearRegression()
lm2.fit(X_train2, y_train2)

y_train_predict2 = lm2.predict(X_train2)
rmse_train2 = (np.sqrt(mean_squared_error(y_train2, y_train_predict2)))
r2_train2 = r2_score(y_train2, y_train_predict2)
print("RMSE_Training_remaining",rmse_train2) #53.338555842312886
print("R2_Training_remaining",r2_train2) #0.5115517387428321

y_test_predict2 = lm2.predict(X_test2)
rmse_test2 = (np.sqrt(mean_squared_error(y_test2, y_test_predict2)))
r2_test2 = r2_score(y_test2, y_test_predict2)
print("RMSE_Test_remaining",rmse_test2) #54.60391290294691
print("R2_Test_remaining",r2_test2) #0.5271558947230806

"""
By adding remaining variables from the dataframe it provides better improvement
in both RMSE and R2 of training and testing sets. R2 of test set has 0.53 and RMSE has 54.60 
it shows that model's performance has improved by adding more variables thus it helps the 
model to feature more variations in the target.

"""


