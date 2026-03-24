l=[1,2,4,5,6,7,8,9]
# list comprehension
s=[i**2 for i in l]
print(s)
l1=["armik","vasu","meet","krishna","hit","prince"]
l2=[i.upper() for i in l1]
print(l2)
x=[i for i in l if i%2==0]
print(x)    

# tuple comprehension
t=("armik","see",23,44,55,)
t1=[i for i in t if type(i)==str]
t2=[i for i in t if type(i)==int]
print(t1)
print(t2)

#dict comprehension
armik={"armik":8,'dhruv':90,'jeel':78,'vasu':56}
ar={i:j*2 for i,j in armik.items()}
print(type(ar))