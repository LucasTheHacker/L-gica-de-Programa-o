#Recebe string
#Escreve os números por extenso
dicionario = {'zero': '0', 'um': '1', 'dois': '2', 'três': '3', 'quatro': '4', 'cinco': '5', 'seis': '6', 'sete': '7', 'oito': '8', 'nove':'9'}
#dicionário pra linkar a palavra por extenso ao seu valor que deve ser escrito
numeros = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
#lista para percorrer a string procurando cada um dos extensos
string = input()
string_normalizada = string.lower() 
tamanho = len(string)
contador = 0
while contador <= 10:
    if string.find(numeros[contador]):
        palavra = str(numeros[contador])
        string = string.replace(palavra, dicionario[numeros[contador]]) #utilização do método replace
        #semântica do replace com dicionários é:, substitua a str, pelo valor dessa str no dicionario
    contador +=1
        
print(string)