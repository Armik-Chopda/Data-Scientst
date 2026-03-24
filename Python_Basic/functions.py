def test():
    print("Hello, my self armik")
test()

def test1():
    return "hello ,my self "
print(test1()+"armik")

def test3():
    return "armik",1256,["ar",33,"gg"]
a,b,c=test3()
print(a)
print(b)
print(c)

def test4():
    a=3*10/9
    return a
print(test4())

def test5(c,b,g):
    a=c+b+g
    return a
print(test5(10,23,45))


li=[1,23,4,5,"armik","fghj",'sdfghj',[8,7,5,3,0,2,3]]
def test6(a):
    li1=[]
    for i in a:
        if type(i)==int:
            li1.append(i)
        if type(i)==list:
            for j in i:
                li1.append(j)
    return li1
print(test6(li))


