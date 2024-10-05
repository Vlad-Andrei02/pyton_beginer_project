import random

def deposit():
    while(True):
        amount = input("How much would you like to deposit?$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount

def get_amount_invested():
    while(True):
        amount = input("How much would you like to invest?$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")    
             
    return amount

def get_investment_period():
    while(True):
        period = input("For how many years do you want to invest? ")
        if period.isdigit():
            period = int(period)
            if period > 0:
                break
            else:
                print("Investment period must be greater than 0.")
        else:
            print("Please enter a valid number.")
    
    return period

def simulate_stock_growth(investment, years):
    # Simulate the stock market with a random growth/decline percentage each year
    annual_growth_rate = random.uniform(-0.2, 0.2)  # -20% to +20% change per year
    total_growth = 1
    for _ in range(years):
        growth_factor = 1 + annual_growth_rate
        total_growth *= growth_factor
    
    final_value = investment * total_growth
    return final_value, annual_growth_rate * 100

def main():
    balance = deposit()
    while True:
        # Loop for multiple simulations
        while True:
            money_invested = get_amount_invested()
            
            if money_invested > balance:
                print(f"You don't have enough to invest that amount, your current balance is: ${balance}")
            else:
                break
        
        print(f"Your current investment is: ${money_invested}")  
        
        investment_period = get_investment_period()
        final_value, annual_rate = simulate_stock_growth(money_invested, investment_period)
        
        print(f"Predicted value after {investment_period} years: ${final_value:.2f}")
        print(f"Average annual growth rate: {annual_rate:.2f}%")
        
        # Ask the user if they want to run another simulation
        repeat = input("Would you like to run another simulation? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the investment simulator. Goodbye!")
            break

main()
