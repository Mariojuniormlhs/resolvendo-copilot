# SOLICITAR AO USUÁRIO UMA STRING E UM VALOR INTEIRO
# A STRING DEVE SER REPETIDA DE ACORDO COM O NUMERO INTEIRO

#RECEBE AS INFORMAÇOES DO USUÁRIO
Texto = input("Digite a string a ser repetida: ")
xRepetir = int(input("Digite a quantidade de vezes que devemos repetí-la: "))

#REPETE O TEXTO CONFORME VALOR INFORMADO
resultado = " ".join([Texto] * xRepetir)

#MOSTRA O RESULTADO
print("Resultado:",resultado)