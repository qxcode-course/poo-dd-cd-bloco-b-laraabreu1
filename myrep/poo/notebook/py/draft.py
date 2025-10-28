class Notebook:
    def __init__(self): # isso é o construtor em python
        self.__ligado: bool = False # ligado é atributo privado e inicializa com false
    # preencha com os métodos necessários

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("notebook ja está ligado")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else:
            print("notebook ja está desligado")

    def mostrar(self):
        status = "Ligado" if self.__ligado else "Desligado"
        print(f"Status: {status}")

    def usar(self, tempo):
        if not self.__ligado:
            print("erro: ligue o notebook primeiro")
        else:
            print(f"Usando por {tempo} minutos")


notebook = Notebook() # criando notebook
notebook.mostrar()    # msg: Status: Desligado
notebook.usar(10)     # msg: erro: ligue o notebook primeiro
notebook.ligar()      # msg: notebook ligado
notebook.mostrar()    # msg: Status: Ligado
notebook.usar(10)     # msg: Usando por 10 minutos
notebook.desligar()   # msg: notebook desligado
