"""## 1. Sistema de Cálculo de Notas

Uma escola deseja criar um programa para calcular a situação dos estudantes.
O programa deverá utilizar funções para organizar as diferentes etapas do processo.

### Requisitos

Crie uma função para:

1. Receber o nome do estudante.
2. Receber três notas.
3. Calcular a média das notas.
4. Verificar a situação do estudante.

A situação deverá seguir estas regras:

- Média igual ou superior a 7 → Aprovado
- Média entre 5 e 6.9 → Recuperação
- Média abaixo de 5 → Reprovado

O programa deverá apresentar:

- Nome do estudante;
- Notas informadas;
- Média calculada;
- Situação final.

### Funções obrigatórias

O programa deverá possuir, pelo menos:

- Uma função para calcular a média;
- Uma função para verificar a situação;
- Uma função para exibir o resultado."""

def aluno():
    nome = input("Digite o nome do estudante: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aluno aprovado")
    elif media >= 5 and media <= 6.9:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")

aluno()