foods = ('arroz', 'feijão', 'carne', 'batata frita', 'salada')
for food in foods:
    print(food)

foods = ('arroz', 'feijão', 'ovo')
foods[0] = 'pão'
print("O cardapio mudou")
for food in foods:
    print(food)
    