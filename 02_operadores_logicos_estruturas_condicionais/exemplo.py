#AULA: OPERADORES LOGICOS E ESTRUTURAS CONDICIONAIS
#1 OPERADORES LOGICOS

#and
# Todas as condicoes precisam ser verdadeiras

idade = 20
possui_carteira = True

resultado = idade >= 18 and  possui_carteira
print(resultado)


#or
#pelo menos uma condicao precisa ser verdadeira

idade = 16
acompanhado = True

resultado = idade >= 18 or acompanhado
print(resultado)

#not
#inverte o resultado de uma condicao

aluno_matriculado = True
print(not aluno_matriculado)

#2 OPERADORES DE COMPARACAO

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)


#3 ESTRUTURA if

idade = 18
if idade >= 18:
    print("Maior de idade")

#4 ESTRUTURA if / else

idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#ESTRUTURA if / elif / else