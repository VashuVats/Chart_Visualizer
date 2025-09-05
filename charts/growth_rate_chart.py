import matplotlib.pyplot as plt

def plot_growth_rate(ax,years, growth_rate):
    ax.plot(years, growth_rate, marker='o', label="Growth Rate", color='purple')
    ax.set_title("Yearly Growth Rate")
    ax.set_xlabel("Year")
    ax.set_ylabel("Growth Rate (%)")
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
    ax.legend()
