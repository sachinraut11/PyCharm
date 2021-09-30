class Student:
   def m1(self):
       self.a=11
       self.b=21
       self.c=34
       print(self.a)
       print(self.b)
       print(self.c)
s= Student()
s.m1()
print(s.__dict__)
