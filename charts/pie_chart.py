import matplotlib.pyplot as plt

def plot_pie_chart(ax,year, male, female):
    ax.pie(
        [male, female],
        labels=["Male", "Female"],
        autopct='%1.1f%%',
        startangle=90,
        colors=['blue', 'pink'],
        explode=(0.1, 0)
    )
    ax.set_title(f"Gender Distribution ({year})")
