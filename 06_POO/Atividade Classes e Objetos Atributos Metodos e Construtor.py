class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade


    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade}")

cachorro1 = Cachorro("lucca", "poodle", 16)

cachorro1.latir()
cachorro1.mostrar_info()