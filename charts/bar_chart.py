import matplotlib.pyplot as plt

def plot_bar_chart(ax,years, male, female, yearTotal):
    width = 0.25
    ax.bar(years - width, male, label="Male", width=width, color='blue', alpha=0.7)
    ax.bar(years, female, label="Female", width=width, color='pink', alpha=0.7)
    ax.bar(years + width, yearTotal, label="Total", width=width, color='green', alpha=0.7)
    ax.set_title("Male, Female, and Total Students")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Students")
    ax.legend()
