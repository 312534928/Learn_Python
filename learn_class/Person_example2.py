# 采用 委托 的复合结构，管理一个包装的对象并把方法调用传递给它
from Person_example import Person


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.1):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person,attr)
    def __str__(self):
        return str(self.person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    sue.giveRaise(.1)
    print(sue)
    tom = Manager('Tom Jones', 5000)
    tom.giveRaise(.1)
    print(tom.lastName())
    print(tom)
