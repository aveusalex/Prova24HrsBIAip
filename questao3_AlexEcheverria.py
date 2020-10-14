import random


def gera_linhas(lista_palavras, dificuldade):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    linhas = []

    if dificuldade == "easy":
        num_linhas = 15
        num_colunas = 15
    elif dificuldade == "medium":
        num_linhas = 25
        num_colunas = 25
    elif dificuldade == "hard":
        num_linhas = 45
        num_colunas = 45

        for palavra in range(len(lista_palavras)//2, len(lista_palavras)):
            palavra1 = lista_palavras[palavra][::-1]
            lista_palavras[palavra] = palavra1

    else:
        num_linhas = 15
        num_colunas = 15

    for i in range(num_linhas):
        linha = random.choices(alfabeto, k=num_colunas)
        linhas.append(linha)

    for palavra in lista_palavras:
        palavra = palavra.lower()
        lista_auxiliar = []

        for numero_linhas in range(len(linhas)):
            lista_auxiliar.append(numero_linhas)

        numeros_escolha = num_colunas - len(palavra)
        escolha = random.randint(0, numeros_escolha - 1)
        escolha_linha = random.choice(lista_auxiliar)
        lista_auxiliar.remove(escolha_linha)
        linha = linhas[escolha_linha]

        for letra in palavra:
            linha[escolha] = letra
            escolha += 1

    for linha in linhas:
        for letra in linha:
            print(letra, end='  ')
        print("")


def main():
    print("\n\n\nCaça palavras!\n\n")
    print("1 - Fácil\n"
          "2 - Médio\n"
          "3 - Difícil\n")

    escolha = input("Digite o número correspondente à dificuldade desejada: ")

    if escolha == "1":
        escolha = "easy"
    elif escolha == "2":
        escolha = "medium"
    elif escolha == "3":
        escolha = "hard"
    else:
        escolha = "easy"

    print("\n\nSe fácil, digite até 10 palavras de até 12 letras.\n"
          "Se médio, digite até 15 palavras de até 20 letras.\n"
          "Se difícil, digite até 40 palavras, sem erstrição de tamanho.\n"
          "Digite-as separadas por espaço.")

    lista_words = input("\nDigite uma lista de palavras seguindo as regras acima: ").split()
    print()
    gera_linhas(lista_words, escolha)


if __name__ == "__main__":
    main()