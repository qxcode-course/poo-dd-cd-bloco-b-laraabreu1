class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def __str__(self):
        return f"{self.__name}:{self.__age}"


class Motoca:
    def __init__(self, power=1):
        self.power = power
        self.time = 0
        self.person = None

    def __str__(self):
        person_str = f"({self.person})" if self.person else "(empty)"
        return f"power:{self.power}, time:{self.time}, person:{person_str}"

    def enter(self, person: Pessoa):
        if self.person is not None:
            print("fail: busy motorcycle")
            return False
        self.person = person
        return True

    def leave(self):
        if self.person is None:
            print("fail: empty motorcycle")
            return None
        removed = self.person
        self.person = None
        print(removed)
        return removed

    def buy(self, time: int):
        self.time += time

    def drive(self, time: int):
        if self.time == 0:
            print("fail: buy time first")
            return
        if self.person is None:
            print("fail: empty motorcycle")
            return
        if self.person.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.time:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0
        else:
            self.time -= time


    def honk(self):
        return "P" + ("e" * self.power) + "m"


def main():
    moto = Motoca()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        if args[0] == "init":
            moto = Motoca(int(args[1]))
        elif moto is None:
            print("fail: moto nao inicializada")
            continue

        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            name = args[1]
            age = int(args[2])
            person = Pessoa(name, age)
            moto.enter(person)
        elif args[0] == "leave":
            moto.leave()
        elif args[0] == "buy":
            moto.buy(int(args[1]))
        elif args[0] == "drive":
            moto.drive(int(args[1]))
        elif args[0] == "honk":
            print(moto.honk())
        else:
            print("fail: comando invalido")


main()