# código do Tempo
# 1. usar o __ no começo pra definir private
# 2. criar um get_algo para leitura e retornar o valor
# 3. criar um set_algo que recebe um valor
# 4. parametros default utilizados quando o valor não vem
# 5. parametros nomeados quando quero um valor especifico

class Tempo:
    def __init__(self, hora: int = 0, min: int = 0):
        self.__h = 0
        self.set_hora(hora)
        self.__m = min
        self.__s = 0

    def set_hora(self, valor: int) -> None: # escrita
        if valor > 11 or valor < 0:
            print("hora errada")
            return
        self.__h = valor

    def get_hora(self) -> int: # leitura
        return self.__h

    def __str__(self):
        return f"{self.__h}:{self.__m}:{self.__s}"

agora = Tempo(min=55, hora=9)
print(agora)