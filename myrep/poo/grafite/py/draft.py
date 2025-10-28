class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size: int = size

    def usagePersheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
        return 0
        
    def get_thickness(self) -> float:
        return self.__thickness
    
    def get_hardness(self) -> str:
        return self.__hardness
    
    def get_size(self) -> int:
        return self.__size
    
    def set_size(self, tamanho: int):
        self.__size = tamanho

    def decrease_size(self, amount: int):
        self.__size -= amount
        if self.__size < 0:
            self.__size = 0

    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
class Pencil:
    def __init__(self, thickness: float = 0, tip: Grafite | None = None):
        self.__thickness = thickness
        self.__tip = tip

    def get_tip(self) -> Grafite | None:
        return self.__tip

    def get_thickness(self) -> float:
        return self.__thickness

    def has_grafite(self) -> bool:
        return self.__tip is not None

    def insert(self, tip: Grafite):
        if self.__tip is not None:
            print("fail: ja existe grafite")
            return
        if tip.get_thickness() != self.__thickness:
            print("fail: calibre incompativel")
            return
        self.__tip = tip

    def remove(self) -> Grafite | None:
        if self.__tip is None:
            print("fail: nao existe grafite")
            return None
        aux = self.__tip
        self.__tip = None
        return aux

    def writePage(self):
        if not self.has_grafite():
            print("fail: nao existe grafite")
            return
            
        gastoPorFolha = self.__tip.usagePersheet() 
        tamanhoAtual = self.__tip.get_size()
        
        if tamanhoAtual <= 0:
            self.remove()
            print("fail: nao existe grafite")
            return
        tamanhoAposEscrita = tamanhoAtual - gastoPorFolha
        if tamanhoAposEscrita <= 10:
            if tamanhoAtual <= 10:
                print("fail: tamanho insuficiente")
                return
            gastoEfetivo = tamanhoAtual - 10
            self.__tip.decrease_size(gastoEfetivo)
            if tamanhoAposEscrita == 10:
                print("fail: tamanho insuficiente")
                return
                print("fail: folha incompleta")
                return
        else:
            self.__tip.decrease_size(gastoPorFolha)

    def __str__(self) -> str:
        return f"calibre: {self.__thickness}, grafite: {self.__tip if self.__tip else 'null'}"


def main():
    pencil = Pencil()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(pencil)

        elif args[0] == "init":
            if len(args) == 2:
                pencil = Pencil(float(args[1]))
            else:
                print("comando iniciar requer calibre")

        elif args[0] == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite = Grafite(thickness, hardness, size)
            pencil.insert(grafite)

        elif args[0] == "remove":
            pencil.remove()

        elif args[0] == "escrever" or args[0] == "write":
            pencil.writePage()

        else:
            print("fail: nao existe grafite")

main()