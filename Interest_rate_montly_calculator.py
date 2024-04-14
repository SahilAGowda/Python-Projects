#collect the necessary input :principal Interest years
#calculate the monthly payment
#show to the user

def main():
    print("This is a Monthly payment Loan Calculator ")
    print("-----------------------------------------")
    
    
    principal=float(input("Enter the Loan Amount : "))
    apr=float(input("Enter the Annual Interest Rate : "))
    year=int(input("Enter the Number of Year : "))
    
    monthly_interest_rate=apr/1200;
    amount_of_months=year*12
    monthly_payment = principal* monthly_interest_rate/(1-(1+monthly_interest_rate)**(-amount_of_months))
    
    print("The Monthly Payment for this Loan is $ %0.2f"%monthly_payment)
    

main()

    
    