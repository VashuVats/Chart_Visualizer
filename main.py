import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from charts.bar_chart import plot_bar_chart
from charts.growth_rate_chart import plot_growth_rate
from charts.percentage_chart import plot_percentage_chart
from charts.pie_chart import plot_pie_chart

data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data.csv"))

years = data["year"].values
male = data["male"].values
female = data["female"].values
yearTotal = data["total"].values

male_percentage = np.divide(male, yearTotal) * 100
female_percentage = np.divide(female, yearTotal) * 100
growth_rate = np.diff(yearTotal) / yearTotal[:-1] * 100
growth_rate = np.insert(growth_rate, 0, 0)

print("Summary Statistics:")
print(f"Total Students (Avg): {np.mean(yearTotal):.2f}")
print(f"Male Students (Avg): {np.mean(male):.2f}")
print(f"Female Students (Avg): {np.mean(female):.2f}")
print(f"Overall Growth Rate (%): {np.mean(growth_rate):.2f}")

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plt.style.use('ggplot')

plot_bar_chart(axes[0, 0], years, male, female, yearTotal)
plot_growth_rate(axes[0, 1], years, growth_rate)
plot_percentage_chart(axes[1, 0], years, male_percentage, female_percentage)
plot_pie_chart(axes[1, 1], years[-1], male[-1], female[-1])

plt.tight_layout()
plt.show()