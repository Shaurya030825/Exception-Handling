try:
    num1= int(input("please enter the first number: "))
    num2= int(input("PLease enter the second number: "))
    result= num1 / num2
    print("Result is:", result)
except ZeroDivisionError:
    print("DIvision by zero is  error!!")
except ValueError:
    print("Please enter whole number")
except:
    print("Wrong INput.")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what.")
    