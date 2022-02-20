# author fc
class Person(object):
    def __new__(cls,*args,**kwargs):
        print("id(cls):{0}".format(id(cls)))
        obj=super().__new__(cls)
        print("id(obj):{0}".format(id(obj)))
        return obj
    def __init__(self,name,age):
        self.name=name
        self.age=age


if __name__=='__main__':
    person=Person("liming",11)
    print("id(person):{0}".format(id(person)))
    print(decode('utf-8'))
