try:
    a=int(input("Enter an integer:"))
    b=int(input("Enter an integer:"))
    c=a/b
    print('c=',c)
except ZeroDivisionError:
    print("Denominator is 0")