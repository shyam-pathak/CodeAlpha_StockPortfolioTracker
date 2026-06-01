available_stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170,
    "META": 200
}

total_investment_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

print("\nAvailable Stocks:")

for stock_name in available_stock_prices:
    print(
        stock_name,
        "- Price:",
        available_stock_prices[stock_name]
    )

number_of_stocks_owned = int(
    input("\nHow many different stocks do you own?, Enter number of stocks. ")
)

for stock_count in range(number_of_stocks_owned):
    stock_name = input(
        "\nEnter Stock Name: "
    ).upper() #y jo input ko upper case me convert kar dega taki user chahe small case me input kare ya capital case me, wo dono case me same stock name ke liye match ho jayega.

    if stock_name in available_stock_prices:

        stock_quantity = int(
            input("Enter Quantity: ")
        )

        stock_value = (
            available_stock_prices[stock_name]
            * stock_quantity
        )

        total_investment_value = (
            total_investment_value
            + stock_value
        )

    else:
        print("Stock not available in portfolio tracker.")

print(
    "\nTotal Investment Value =",
    total_investment_value
)

save_result = input(
    "\nDo you want to save the result in a file? (yes/no): "
).lower()

if save_result == "yes":

    investment_file = open(
        "portfolio_result.txt",
        "w"
    )

    investment_file.write(
        "Total Investment Value = "
        + str(total_investment_value)
    )

    investment_file.close()

    print(
        "Result saved successfully in portfolio_result.txt"
    )