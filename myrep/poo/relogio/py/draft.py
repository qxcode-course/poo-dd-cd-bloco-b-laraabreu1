class Watch:
    def __init__(self, hora = 0, minuto = 0, segundo = 0):
        self.__h = 0
        self.__m = 0
        self.__s = 0
        self.set(hora, minuto, segundo)

    def set_hora(self, hora):
        if 0 <= hora <= 23:
            self.__h = hora
        else:
            print("fail: hora invalida")

    def set_minuto(self, minuto):
        if 0 <= minuto <= 59:
            self.__m = minuto
        else:
            print("fail: minuto invalido")

    def set_segundo(self, segundo):
        if 0 <= segundo <= 59:
            self.__s = segundo
        else:
            print("fail: segundo invalido")

    def set(self, hora, minuto, segundo):
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def nextSecond(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0

    def __str__(self):
        return f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}"


def main():
    relogio = Watch()
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            relogio = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            relogio.set(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.nextSecond()
        else:
            print("fail: comando invalido")

main()
