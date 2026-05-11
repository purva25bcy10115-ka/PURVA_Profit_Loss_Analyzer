import matplotlib.pyplot as plt


def show_graph(months, profits):

    colors = []

    for p in profits:
        if p >= 0:
            colors.append("green")
        else:
            colors.append("red")

    plt.bar(months, profits, color=colors)

    plt.title("Monthly Profit/Loss Report")

    plt.xlabel("Months")

    plt.ylabel("Profit / Loss")

    plt.axhline(0, color='black')

    plt.show()