import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

df = pd.read_csv('Auto.csv')
print(df)

x = df.drop(columns=['mpg','name','origin'])
y = df['mpg']

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size = 0.2, random_state=5)

alphas = [0.1,0.2,0.3,0.4,0.5,1,2,3,4,5,6,7,8]
scores_lasso = []
scores_ridge = []
for alp in alphas:
    lasso = linear_model.Lasso(alpha=alp)
    lasso.fit(x_train, y_train)
    print(lasso.coef_.round(2))
    sc_lasso = lasso.score(x_test, y_test)
    scores_lasso.append(sc_lasso)
    print("alpha=",alp, "lasso score:", sc_lasso)

    ridge = Ridge(alpha=alp)
    ridge.fit(x_train, y_train)
    sc_ridge = ridge.score(x_test, y_test)
    scores_ridge.append(sc_ridge)
    print("alpha=", alp, "ridge score:", sc_ridge)


plt.plot(alphas, scores_lasso, label="Lasso", marker='o')
plt.plot(alphas, scores_ridge, label="Ridge", marker='x')
plt.xlabel('alpha')
plt.ylabel('R2 score')
plt.title('Ridge Vs Lasso Regression: R2 Vs alpha')
plt.show()

best_lasso_alp = alphas[np.argmax(scores_lasso)]
best_ridge_alp = alphas[np.argmax(scores_ridge)]

print("Best alpha for lasso and ridge are:",best_lasso_alp,"and", best_ridge_alp,"respectively.")


"""
Output:
[-0.2   0.01  0.01 -0.01  0.13  0.7 ]
alpha= 0.1 lasso score: 0.7734705894488576
alpha= 0.1 ridge score: 0.7705207220236019
[-0.    0.    0.   -0.01  0.1   0.69]
alpha= 0.2 lasso score: 0.7748211453201694
alpha= 0.2 ridge score: 0.7705248595590017
[-0.    0.    0.   -0.01  0.07  0.68]
alpha= 0.3 lasso score: 0.775009846624372
alpha= 0.3 ridge score: 0.7705289833917044
[-0.    0.   -0.   -0.01  0.05  0.67]
alpha= 0.4 lasso score: 0.7746847678322342
alpha= 0.4 ridge score: 0.7705330935759367
[-0.    0.   -0.   -0.01  0.01  0.66]
alpha= 0.5 lasso score: 0.7746429535277378
alpha= 0.5 ridge score: 0.7705371901656423
[-0.    0.   -0.   -0.01  0.    0.62]
alpha= 1 lasso score: 0.7708170585064884
alpha= 1 ridge score: 0.7705574710647298
[-0.   -0.   -0.01 -0.01  0.    0.53]
alpha= 2 lasso score: 0.7607996430293982
alpha= 2 ridge score: 0.7705970435050602
[-0.   -0.   -0.01 -0.01  0.    0.44]
alpha= 3 lasso score: 0.748335685124867
alpha= 3 ridge score: 0.7706353388907887
[-0.   -0.   -0.01 -0.01  0.    0.35]
alpha= 4 lasso score: 0.7334449328575002
alpha= 4 ridge score: 0.7706724055206803
[-0.   -0.   -0.01 -0.01  0.    0.27]
alpha= 5 lasso score: 0.7161089977954003
alpha= 5 ridge score: 0.7707082893077438
[-0.   -0.   -0.01 -0.01  0.    0.18]
alpha= 6 lasso score: 0.696327968386669
alpha= 6 ridge score: 0.7707430339225424
[-0.   -0.   -0.02 -0.01  0.    0.09]
alpha= 7 lasso score: 0.6741021421828612
alpha= 7 ridge score: 0.7707766809264263
[-0.   -0.   -0.02 -0.01  0.    0.  ]
alpha= 8 lasso score: 0.6494275705371795
alpha= 8 ridge score: 0.7708092698954948
Best alpha for lasso and ridge are: 0.3 and 8 respectively.


In the graph, ridge line appears straight while lasso has curve.
Because in ridge regression, R2 does not change much as alpha increases while in lasso
R2 drops more which tends to make curve.
High R2 score for lasso is near to 0.77 with a small alpha 0.3,
after that the curve decline as alpha increases.
Best R2 score for ridge is 0.77 with alpha 8. For each value of alpha, a ridge
regression model is trained to understand the relation with target 'mpg'.
Training model is tested with R2 score to find predictive value.
Each R2 data has stored so the highest R2's alpha value could be analysed
to determine for the best or optimal predictive accuracy . Similarly with lasso.


"""
