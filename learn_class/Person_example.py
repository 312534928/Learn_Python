class Person():
    '''
    This is Person.__doc__
    '''
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        '''
        This is Person.lastName.__doc__
        :return:
        '''
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, Job: %s, Salary: %s]' % (self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    # 不好的继承方式
    # def giveRaise(self, percent, bonus=0.1):
    #     self.pay = int(self.pay * (1 + percent + bonus))

    # 好的方式
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
        # 类方法可以通过实例来调用
        #     instance.method(arg....)
        # 类方法可以通过类来调用
        #     class.method(instance,arg...)


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
    print(tom.__class__)
    print(Manager.__dict__)
    print(Person.__doc__)
    print(Person.lastName.__doc__)