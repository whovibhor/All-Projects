def arbitrage_betting(odd1, odd2, total_stake=100):
    arb_percentage = (1 / odd1) + (1 / odd2)
    
    if arb_percentage < 1:
        stake1 = (total_stake * (1 / odd1)) / arb_percentage
        stake2 = (total_stake * (1 / odd2)) / arb_percentage
        profit = total_stake * (1 - arb_percentage)
        
        print(f"Arbitrage Exists!\nStake on Odd {odd1}: {round(stake1, 2)}\nStake on Odd {odd2}: {round(stake2, 2)}\nGuaranteed Profit: {round(profit, 2)}")
    else:
        print("No arbitrage opportunity.")

# Get user input
odd1 = float(input("Enter first odd: "))
odd2 = float(input("Enter second odd: "))

arbitrage_betting(odd1, odd2)