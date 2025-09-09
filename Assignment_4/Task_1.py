import matplotlib.pyplot as plt
import numpy as np

#n_values = [500,1000,2000,5000,10000,15000,20000,50000,100000]
n_values = [100,200,300,400,500]
for n in n_values:
    dice1 = np.random.randint(1,7,n)
    dice2 = np.random.randint(1,7,n)
    total = dice1+dice2

    h,h2 = np.histogram(total, np.arange(2,14))

    plt.bar(h2[:-1], h/n, align='center', color="blue")
    plt.title(f"Dice sums ={n}")
    plt.xlabel("Sum of the dice")
    plt.ylabel("Probability")
    plt.show()


  #4. As we run the loop small values of n like 100,200...500
  # probabilities bar appeared as uneven, there is a fluctuations or variations in the sum of dices by running loop each time.
  # For large values of n like 500,1000...100000  the distribution of probability is in triangular form
  # with stability means highest shown in 0.16 and lowest at 0.24 in every run of loop.
  

#5.  I examined that as the value of n is small like 100,200.... bars are irregular and did not match with distribution
# As  values of n is medium like 2000..15000 bars having alignment with distribution
# And as n becomes large like 50000...100000 bars perfectly reflect with distribution.
# we can say fluctuations become smaller as the number of trials increases.
# So,random deviation decrease as sample size increase.
# with more dice rolls, the distribution of probabilities is more stable,

