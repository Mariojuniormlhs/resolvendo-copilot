#RECEBEREMOS UMA STRING DO USER E VAMOS IDENTIFICAR SE É UM PALINDROMO

#RECEBE A PALAVRA INFORMADA
string = input("Digite sua palavra ou frase: ")


#REMOÇAO DE ESPAÇOS
formated_string = string.replace(" ", "").lower()

# Verifica se a palavra é um palíndromo
if formated_string == formated_string[::-1]:
    print("A palavra ou frase "+string+" é um palíndromo.")
else:
    print("A palavra ou frase "+string+" não é um palíndromo.")