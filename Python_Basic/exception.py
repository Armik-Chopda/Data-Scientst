a=int(input("enter number"))
try:
    print(a/0)
except ZeroDivisionError as e:
    print("hello " ,e)
else:
    print("error not found")         
finally:
    print("armik")
    



