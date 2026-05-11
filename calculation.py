def calculate_profit(production, cost_per_unit,
                     selling_price, other_expenses):

    total_cost = (production * cost_per_unit) + other_expenses

    revenue = production * selling_price

    profit = revenue - total_cost

    return total_cost, revenue, profit