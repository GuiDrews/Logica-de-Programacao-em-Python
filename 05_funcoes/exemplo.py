#O que é uma função?

#Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem vindo!")

saudacao()

#2. Criando uma função com parâmetro
#parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Olá {nome}")

saudacao("Ana")
saudacao("João")

#3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar(nome = "Maria", idade = 17)
apresentar(nome = "João", idade = 18)

#4. Função com calculo

def somar(num1, num2):
    resultado = num1 + num2
    print(f"Resultado {resultado}")
somar(num1 = 10, num2 = 20)
somar(num1 = 10, num2 = 90)

#5. Retornando um valor
#return devolve um valor par ao local onde a função foi chamada
def somar(num1, num2):
    return num1 + num2

print(somar(num1 = 10, num2 = 5))

#6. Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

print(verificarIdade(20))

#7. Parâmetro com valor padrão
def saudacao(nome = "Aluno"):
    print(f"Ola {nome}")

saudacao("João")
saudacao()

#8. Função utilizando lista
def calcularMedia():
    for nota in notas:
        soma += nota
    return soma / len(notas)

notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"média: {media}")