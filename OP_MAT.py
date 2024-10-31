#VAMOS RECEBER DOIS NÚMEROS E APLICAREMOS AS OPERAÇOES MATEMATICAS PARA ESSES DADOS RECEBIDOS

#RECEBE OS DADOS DO USUÁRIO
valor1 = int(input("Digite um valor numérico: "))
valor2 = int(input("Digite o segundo valor numérico: "))

operacao = input("Digite qual a operação você deseja realizar (+,-,*,/): ")

if operacao == '+':
    print(valor1 + valor2)

elif operacao == '-':
    print(valor1 - valor2)

elif operacao == '*':
    print(valor1 * valor2)

elif operacao == '/':
    print(valor1 / valor2)

else: print("Operação Inválida!")