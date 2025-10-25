class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():
    roupa = Camisa()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            roupa = Camisa()
        elif args[0] == "show":
            print(f"size: ({roupa.getTamanho()})")
        elif args[0] == "size":
            if len(args) > 1:
                roupa.setTamanho(args[1])
            else:
                print("fail: nenhum tamanho informado")

main()