class test1:
    def class1(self):
        return " this my class one"
class test2(test1):
    def class2(self):
        return "this is my class two"
class test3(test2):
    def class3(self):
        pass
obj=test3()
print(obj.class2())
print(obj.class1())
