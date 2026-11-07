valid= False
while not valid:
    try:
        n= int(input("Please neter a number: "))
        while n % 2==0:
            print("Bye")
            n= int(input("Please enter a  number: "))
        valid= True
    except ValueError:
        print("Invalid")
