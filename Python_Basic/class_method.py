class data:
    id=1001
    def __init__(self,name,email):
        self.name=name
        self.email=email
    @classmethod
    def student(cle,number,email,name):

        return cle(email,name)
    @classmethod
    def id(abc,ID):
        data.id=ID
        return data.id
    def prints(self):
        print(self.name,self.email,data.id)

def details(cle,course):
    return course

n1=data("armik","chopda")
n=data.student("123456890","iwiwiw","wwww")
data.details=classmethod(details) 
data.id(922)
x=data.details("1112")
print(n.name)
print(n1.email,n1.name)
print(data.id)
n1.prints()
print(x)

