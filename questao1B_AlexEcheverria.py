def calcula_fracao(valor_total, massa_total, massa_parcial):
    valor_fracao = valor_total * (massa_parcial/massa_total)

    return valor_fracao


# Armazena o valor das massas do pacote de cada ingrediente e a massa a ser utilizada na receita (aproximada).
def dados_pacotes_inteiros(index):

    lista_ingredientes = ["agua", 'fermento', 'oleo', 'sal', 'acuca_mascavo', 'aveia',
                          'germen', 'linhaca', 'farinha_trigo']

    database = {"agua": [1000, 400],
                'fermento': [50, 25],
                'oleo': [1000, 100],
                'sal': [1000, 8],
                'acuca_mascavo': [1000, 20],
                'aveia': [1000, 200],
                'germen': [1000, 100],
                'linhaca': [1000, 100],
                'farinha_trigo': [1000, 400]
                }

    ingrediente = lista_ingredientes[index]

    return database[ingrediente]


def main():
    preco = 0
    valores = []
    print("\n\n\nCalcula lucro!\n\n")
    valores.append(float(input("Insira o valor do litro d'agua: R$")))
    valores.append(float(input("\nInsira o valor do pacote de fermento: R$")))
    valores.append(float(input("\nInsira o valor do litro de oleo: R$")))
    valores.append(float(input("\nInsira o valor do quilo de sal: R$")))
    valores.append(float(input("\nInsira o valor do quilo do acucar mascavo: R$")))
    valores.append(float(input("\nInsira o valor do quilo de aveia: R$")))
    valores.append(float(input("\nInsira o valor do quilo de germen de trigo: R$")))
    valores.append(float(input("\nInsira o valor do quilo de semente de linhaca: R$")))
    valores.append(float(input("\nInsira o valor do quilo da farinha de trigo: R$")))

    for index in range(0, 9):
        lista_massas = dados_pacotes_inteiros(index)
        valor = valores[index]
        preco += calcula_fracao(valor, lista_massas[0], lista_massas[1])

    preco = 1.15 * preco

    print(f"\n\nO custo de cada fornada de pão integral é: R${preco:.2f}")


if __name__ == "__main__":
    main()
