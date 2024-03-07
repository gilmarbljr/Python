class Automovel:
    self.nome
    self.ano
    self.placa
    self.valor

    def __init__ (self, nome : str = None, ano : int = 0, placa : str = None, valor : float = 0.0):
        self.setNome(nome)
        self.setAno(ano)
        self.setPlaca(placa)
        self.setValor(valor)
    
    def setNome(self, nome : str):
        raise NotImplementedError("This Method Must Be Implemented")

    def setAno(self, ano : int):
        raise NotImplementedError("This Method Must Be Implemented")

    def setPlaca(self, placa : str):
        raise NotImplementedError("This Method Must Be Implemented")
    
    def setValor(self, valor : float):
        raise NotImplementedError("This Method Must Be Implemented")

    def getNome(self) -> str:
        return self.nome

    def getAno(self) -> int:
        return self.ano

    def getPlaca(self) -> str:
        return self.placa

    def getValor(self) -> float:
        return self.valor