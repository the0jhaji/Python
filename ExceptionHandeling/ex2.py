try:
    a=int(input("Enter an integer:"))
    b=int(input("Enter an integer:"))
    c=a/b
    print('c=',c)
except ZeroDivisionError:
    print("Denominator is 0")
    print(zde.args)
    print(zde)
except ValueError:
    print('enable to convert string to int')
except:
    print("some unknown error")