a=int(input("enter number"))
try:
    print(a/0)
except ZeroDivisionError as e:
    print("hello " ,e)
else:
    print("error not found")         
finally:
    print("armik")

try:
    import armik
except ImportError as e:
    print(e)


    
try:
    d={"id":1,"name":"armik","email":"armik@gmail.com"}
    print(d['idw'])
except KeyError as e:
    print(e)


try:
    "armik".test()
except AttributeError as a:
    print(a)   

try:
    l=[1,2,3,4,4]
    print(l[8])
except IndexError as e:
    print(e)            


try:
    12+"qww"
except TypeError as e:
    print(e)   


try:
    with open("armik.txt",'r') as f:
        f.read()
except FileNotFoundError as e:
    print(e)  

print(dir(Exception) )   

try:
    l=[1,2]
    print(l[3])
   
except IndexError as e:
    print("armik",e)   
except Exception as e:
    print(e)    



