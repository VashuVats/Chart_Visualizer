import matplotlib.pyplot as plt

def plot_percentage_chart(ax,years, male_percentage, female_percentage):
    ax.bar(years, male_percentage, label="Male %", color='blue', alpha=0.7)
    ax.bar(years, female_percentage, bottom=male_percentage, label="Female %", color='pink', alpha=0.7)
    ax.set_title("Male vs Female Percentage")
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage")
    ax.legend()
