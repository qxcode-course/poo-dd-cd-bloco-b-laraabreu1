class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("Erro: tamanho inválido! O tamanho deve estar entre 20 e 50.")
        elif valor % 2 != 0:
            print("Erro: o tamanho deve ser um número par!")
        else:
            self.__tamanho = valor

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        print("Digite o tamanho da chinela")
        tamanho = int(36)
        chinela.setTamanho(tamanho)
    print(f"Parabéns! Você comprou uma chinela tamanho {chinela.getTamanho()}.")

main()