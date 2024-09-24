def calculate_interest(principal_amount, interest_rate, investment_time, result):

    print(
        f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${result:,.2f}"
    )


principal_amount = input("enter the princaple amount: ")
interest_rate = input("enter the interest rate as a whole number: ")
investment_time = input("enter the investment time in years: ")
result = print(principal_amount * interest_rate * investment_time)

calculate_interest(principal_amount, interest_rate, investment_time, result)
