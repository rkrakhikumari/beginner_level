try:
   # answer = 10/0
    number = int(input("enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except:
    print("invalid input")