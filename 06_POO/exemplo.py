# A CLASSE: O modelo(a planta)
from types import coroutine


class Celular:
    def __init__(self, marca, modelo, cor, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

# Objetos: Criados apartir da classe ("as casas")

celular1 = Celular("Sansung", "Galaxy s23", "Preto")
celular2 = Celular("Motorola", "MotoG", "Azul")

# Acessando e alterando atributos
print(celular1.marca)

# podemos alterar diretamente
celular1.cor = "branco"
print(celular1.cor)

#Chamando métodos
celular2.ligar()