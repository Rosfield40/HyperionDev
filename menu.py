menu = ['coffee', 'tea', 'latte', 'iced frappe'] #list for menu items

#dictionary for stock of each item
stock = {
    'coffee': 16,
    'tea': 8,
    'latte': 5,
    'iced frappe': 8
}

#dictionary for cost of each item
price = {
    'coffee': 4,
    'tea': 3,
    'latte': 5,
    'iced frappe': 3.5
}

#string set to 0 for total stock price calculation
total_stock_worth = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value


print("Total stock worth in the cafe: $", total_stock_worth)