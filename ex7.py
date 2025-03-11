def somatorio(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + somatorio(lista[1:])

# Testando a função com alguns exemplos
lista = [1, 2, 3, 4, 5]
print("Somatório:", somatorio(lista))  # Resultado esperado: 15