def is_leap_year(year):
    if year %4 == 0:
        if year %100 ==0:
            if year % 400 ==0:
                print("Leap Year")
            else:
                print("Not a Leap Year")    
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")
        
print("Welcome to the leap Year Checking Program")
year=int(input("Enter the Year to be checked "))       
is_leap_year(year)