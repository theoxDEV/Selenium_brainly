def intersecao(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n in lista2:
            lista3.append(n)
    return lista3
    
lista1 = ["Thoox", "T", "Thuux"]
lista2 = ["AAAA", "Thoox", "Thuux"]
string_A = intersecao(lista1, lista2)
print(string_A)
