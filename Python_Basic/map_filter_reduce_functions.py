from functools import reduce
l=[1,2,3,4,5,6]
# normal function 
def sqr(l):
    li=[]
    for i in l:
        li.append(i**2)
    return li
print(sqr(l))
#map function
def sq(x):
    return x**2
print(list(map(sq,l)))

# map with lambda function
print(list(map(lambda x:x**2,l)))

l1=[5,6,3,4,7,3]
l2=[3,5,2,7,9,3]
print(list(map(lambda x,y:x+y,l1,l2)))

armik="i am armik"
print(list(map(lambda a:a.upper(),armik)))

# reduce
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x*y,l))
print(reduce(lambda x,y:x if x>y else y,l))

# filter
print(list(filter(lambda x:x%2==0,l)))
l3=[-2,-4,-2,-4,5,8,4,6,0]
print(list(filter(lambda x:x<0,l3)))

names=['armik','ravi','vasu','het','aakash','jeel']
print(list(filter(lambda x:len(x)<5,names)))