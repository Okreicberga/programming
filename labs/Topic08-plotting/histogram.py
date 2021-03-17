# Proram that plotsa histogram of the salaries

# Autor Olga Kreicberga

import numpy as np 
import matplotlib.pyplot as plt 


minSalary = 20000
maxSalary = 80000
numberofEntries = 10
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberofEntries)

plt.hist(salaries)
plt.show()
