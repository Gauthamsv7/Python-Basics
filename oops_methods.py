class Student:

    school = "Ramakrishna"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("Hi There")

s1 = Student(4,5,6)
s2 = Student(7,8,9)

print(s1.avg())
print(Student.get_school())
Student.info()