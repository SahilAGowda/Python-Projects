def main():
    print("This program converts the Us dollar into Indian Rupees ")
    print("=====================================================")
    dollars=eval(input("Enter the amount in dollars"))
    rupee=convert_to_rupee(dollars)
    
    print("That is ",rupee,"Rupee")
    
convert_to_rupee=lambda dollar:dollar*83.61

main()