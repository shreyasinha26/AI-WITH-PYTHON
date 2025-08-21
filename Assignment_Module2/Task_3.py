import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("weight-height.csv")
print(df.head())

length = df['Height'].values
weight = df['Weight'].values

length_cm = length * 2.54
weight_kilo = weight * 0.453592
print(length_cm, weight_kilo)

l_mean = np.mean(length_cm)
w_mean = np.mean(weight_kilo)

print(f"Mean(Length):{l_mean:.2f}cm\nMean(Weight):{w_mean:.2f}kg ")

plt.hist(length_cm,color='blue',edgecolor='black')
plt.xlabel('Length in cm')
plt.ylabel('Number of students')
plt.title('Histogram of Student Lengths')
plt.show()



