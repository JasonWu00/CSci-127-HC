#Name: CSci 127 Bronx team
#Email: 
#Date: October 21, 2020
#NOTE: This is the framework from homework 27. Edit it to fit our purposes.

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Borough: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("Min: ", pop[borough].min())
print("Max: ", pop[borough].max())
print("Mean: ", pop[borough].mean())
print("Median: ", pop[borough].median())
print("Standard Deviation: ", pop[borough].std())
