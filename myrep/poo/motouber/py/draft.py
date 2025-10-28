class Person:
    def __init__(self, name: str, money: int):
        self.__name = name
        self.__money = money

    def get_name(self):
        return self.__name

    def get_money(self):
        return self.__money

    def set_money(self, value: int):
        self.__money = value

    def pay(self, value: int) -> int:
        paid = min(self.__money, value)
        self.__money -= paid
        return paid

    def __str__(self):
        return f"{self.__name}:{self.__money}"


class Moto:
    def __init__(self):
        self.__cost = 0
        self.__driver = None
        self.__passenger = None

    def set_driver(self, person: Person):
        self.__driver = person

    def set_passenger(self, person: Person):
        self.__passenger = person

    def drive(self, km: int):
        if self.__driver is None:
            print("fail: no driver")
            return
        if self.__passenger is None:
            print("fail: no passenger")
            return
        if km <= 0:
            print("fail: invalid distance")
            return
        self.__cost += km

    def leave_passenger(self):
        if self.__passenger is None:
            print("fail: no passenger")
            return
        passenger = self.__passenger
        driver = self.__driver
        cost = self.__cost
        if passenger.get_money() < cost:
            print("fail: Passenger does not have enough money")
        paid = passenger.pay(cost)
        driver.set_money(driver.get_money() + cost)
        print(f"{passenger.get_name()}:{passenger.get_money()} left")
        self.__cost = 0
        self.__passenger = None

    def show(self):
        driver = str(self.__driver) if self.__driver else "None"
        passenger = str(self.__passenger) if self.__passenger else "None"
        print(f"Cost: {self.__cost}, Driver: {driver}, Passenger: {passenger}")

    def __str__(self):
        driver = str(self.__driver) if self.__driver else "None"
        passenger = str(self.__passenger) if self.__passenger else "None"
        return f"Cost: {self.__cost}, Driver: {driver}, Passenger: {passenger}"


def main():
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            name = args[1]
            money = int(args[2])
            driver = Person(name, money)
            moto.set_driver(driver)
        elif args[0] == "setPass":
            name = args[1]
            money = int(args[2])
            passenger = Person(name, money)
            moto.set_passenger(passenger)
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leave_passenger()
        else:
            print("fail: comando inválido")

main()