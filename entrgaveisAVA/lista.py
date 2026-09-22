def adicionar_item(lista, item):
    nova_lista = lista.copy()
    nova_lista.append(item)

    return nova_lista


notas = [7, 8, 9]

resultado = adicionar_item(notas, 10)

print(resultado)
print(notas)
