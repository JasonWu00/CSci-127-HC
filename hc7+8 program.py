#Name: CSci 127 Bronx team
#Email: 
#Date: October 21, 2020
#NOTE: This is the framework from homework 27. Edit it to fit our purposes.

import matplotlib.pyplot as plt
import pandas as pd

firstBorough = input("First borough: ")
secondBorough = input("Second borough: ")
filename = input("File name: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop["Fraction"] = (pop[firstBorough] + pop[secondBorough]) / pop["Total"]
pop.plot(x="Year", y="Fraction")

plt.show()

plt.savefig(filename)

