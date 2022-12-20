def fibonacci(n):
    indice = 1
    base_0 = 0
    base_1 = 1
    caso_n = 0
    while indice <= n:
        print(caso_n, end=" ")
        base_0 = base_1 #transforma o primeiro termo no segundo
        base_1 = caso_n #o 'último' valor passa a ser o último que foi printado
        caso_n = base_1 + base_0 #o próximo elemento a ser printaado é a lógica do fibonacci
        indice += 1