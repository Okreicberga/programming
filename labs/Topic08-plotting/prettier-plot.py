# Program that makes a list called ages that has, the same number random values as salaries
# with label to the plot and label on the axis 

# Autor Olga Kreicberga

import numpy as np 
import matplotlib.pyplot as plt 


minSalary = 20000
maxSalary = 80000
numberofEntries = 10
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberofEntries)
ages = np.random.randint(low=21, high = 65, size = numberofEntries)

plt.scatter(ages, salaries, label="salaries") # this will be random 
# plt.show()

# add x squared 
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints,ypoints, color= 'r', label = "x squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()


plt.savefig('prettier-plot.png')
plt.show() 