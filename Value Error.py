try:
    number= int(input("Please enter a number: "))
    print("The entered number is", number)

except ValueError as ex:
    print("Exception:", ex)