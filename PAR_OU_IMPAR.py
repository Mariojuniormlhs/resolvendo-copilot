#VAMOS RECEBER UM VALOR NUMÉRICO DO USUÁRIO E INFORMAR SE ESTE É IMPAR OU PAR

#RECEBE O VALOR DO USUÁRIO
valor1 = int(input("Digite o valor a ser verificado: "))

#INFORMA SE O NUMERO É PAR OU IMPAR (OTIMIZAÇAO SUGERIDA PELO CHATGPT)
print("O número é par." if valor1 % 2 == 0 else "O número é ímpar.")

#if valor1 % 2 == 0:
#    print("Este número é par!")
#
#else:
#    print("Este número é impar!")