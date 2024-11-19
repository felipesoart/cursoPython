class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("Carro já esta ligado, nada acontece")
        else:
            print(f"{self.modelo} ligado")
            self.ligado = True
    
    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} desligado")
            self.ligado = False    
        else:
             print("Carro já esta desligado, nada acontece")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possivel acelarar, o carro desligado")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possivel frear, o carro desligado")
