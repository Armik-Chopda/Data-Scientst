def test_fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in test_fib(10):
    print(i)



def count(n):
    counts=1
    while counts<=n:
        yield counts
        counts=counts+1
c=count(10)
for i in c:
    print(i)

