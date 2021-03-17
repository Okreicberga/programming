# Proram that makes a list - called Sallaries, 
# that has (say 10) random numbers (20000-80000)
# Autor Olga Kreicberga

import numpy as np 


minSalary = 20000
maxSalary = 80000
numberofEntries = 10
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberofEntries)
salariesMult = salaries * 1.05

newSalaries = salariesMult.astype(int) # convert to an Int array 
print(newSalaries)