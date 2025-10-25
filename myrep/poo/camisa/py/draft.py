class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("Tamanho de roupa não existente, digite um dos tamanhos: PP, P, M, G, GG ou XG")

def main():
    roupa = Camisa()
    while roupa.getTamanho() == "":
        print("Digite seu tamanho de roupa")
        tamanho = "P"
        roupa.setTamanho(tamanho)
    print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())

main()