import abc
class university:
    @abc.abstractmethod
    def student_ditials(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass
class student(university):
    def student_ditials(self):
        return "this is my student ditials"
    def student_assignment(self):
        return "my sudent assignment id pending"
class student2(university):
    def student_ditials(self):
        return "dkedni" 
    def student_marks(self):
        return 23
s2=student2()
s1=student()
print(s2.student_marks())
print(s2.student_ditials())
print(s1.student_assignment())
print(s1.student_ditials())


