"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)


plt.style.use('ggplot')

data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))

years = data["year"]
male = data["male"]
female = data["female"]
yearTotal = data["total"]

width = 0.3

#MALE
plt.bar(years-width,male, label="male",width=width)
#FEMALE
plt.bar(years+width,female, label="female",width=width)
#TOTAL
plt.bar(years,yearTotal, label="Total",width=width)

plt.title('student taking exam')
plt.xticks(ticks=years,labels=years, rotation=45)
plt.xlabel('Year')
plt.ylabel('Number of students')
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.show()


"""