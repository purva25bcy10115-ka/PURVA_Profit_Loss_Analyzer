from calculation import calculate_profit
from graph import show_graph
import csv


months = []
profits = []

num = int(input("Enter number of months: "))

for i in range(num):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")

    production = int(input("Enter production quantity: "))

    cost_per_unit = float(input("Enter cost per unit: "))

    selling_price = float(input("Enter selling price per unit: "))

    other_expenses = float(input("Enter other expenses: "))

    total_cost, revenue, profit = calculate_profit(
        production,
        cost_per_unit,
        selling_price,
        other_expenses
    )

    months.append(month)
    profits.append(profit)

    print("\n----- Report -----")
    print("Revenue:", revenue)
    print("Total Cost:", total_cost)

    if profit >= 0:
        print("Profit:", profit)
    else:
        print("Loss:", profit)

    with open("data.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            month,
            production,
            total_cost,
            revenue,
            profit
        ])


show_graph(months, profits)