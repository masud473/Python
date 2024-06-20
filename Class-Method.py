class Employee:
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age

    @classmethod
    def miner(cls, info):
        return cls(info.split(",")[0], info.split(",")[1], info.split(",")[2])

    def show(self):
        print(self.name, self.salary, self.age)


test = Employee.miner("Farhan,12000,21")
print(test.__dict__)
