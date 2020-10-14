from datetime import datetime, date, timedelta


def horas_em_minutos(hora):
    hora = hora.split('h')
    minutos = int(hora[1])
    horas = int(hora[0])
    minutos += horas * 60

    return minutos


def minutos_para_horas(minutos):
    horas = minutos // 60
    minutos_excendentes = minutos % 60

    return horas, minutos_excendentes


def calcula_dias(dia1, dia2):
    data_inicio = datetime.strptime(dia1, "%d/%m/%Y")
    data_fim = datetime.strptime(dia2, "%d/%m/%Y")

    quantidade = abs((data_inicio - data_fim).days)
    return quantidade


def calcula_com_horas(dia1, dia2, hora1, hora2):
    dias = calcula_dias(dia1, dia2)
    dias_em_minutos = dias * 24 * 60
    hora_inicio = horas_em_minutos(hora1)
    hora_fim = horas_em_minutos(hora2)
    dias_em_minutos = dias_em_minutos - hora_inicio - (24*60 - hora_fim)
    lista_horas_minutos = minutos_para_horas(dias_em_minutos)
    dias = lista_horas_minutos[0] // 24
    horas = lista_horas_minutos[0] % 24
    minutos = lista_horas_minutos[1]

    return dias, horas, minutos


def soma_dias_a_uma_data(data, dias):
    data = data.split('/')
    dia = date(int(data[2]), int(data[1]), int(data[0]))

    if dias < 0:
        dia = dia - timedelta(abs(dias))
    else:
        dia = dia + timedelta(dias)

    dia = str(dia).split("-")
    return dia


def main():
    print("\n\n\nCalculadora de datas!\n\n")
    print("1 - Calcular diferença de datas\n"
          "2 - Calcular diferença de datas com horas\n"
          "3 - Somar dias a uma data\n")
    escolha = input('Digite o número correspondente ao que deseja: ')
    if escolha == "1":
        primeira_data = input("Digite a primeira data (siga o padrão DD/MM/AAAA): ")
        segunda_data = input("Digite a segunda data (siga o padrão DD/MM/AAAA): ")
        dias = calcula_dias(primeira_data, segunda_data)
        print(f"\nA diferença entre as duas datas é {dias} dias.")

    elif escolha == "2":
        primeira_data = input("Digite a primeira data (siga o padrão DD/MM/AAAA): ")
        primeira_hora = input("Digite a hora da primeira data (siga o padrão HHhMM, 09h45): ")
        segunda_data = input("Digite a segunda data (siga o padrão DD/MM/AAAA): ")
        segunda_hora = input("Digite a hora da segunda data (siga o padrão HHhMM, 09h45): ")
        lista_aux = calcula_com_horas(primeira_data, segunda_data, primeira_hora, segunda_hora)
        print(f"\nA diferença entre as datas é de {lista_aux[0]} dias, {lista_aux[1]} horas e {lista_aux[2]} minutos.")

    elif escolha == "3":
        data = input("Digite a data (siga o padrão DD/MM/AAAA): ")
        dias = int(input("Digite a quantidade de dias a se somar ou subrair (digite um número negativo para subtrair): "))
        dia = soma_dias_a_uma_data(data, dias)
        print(f"\nO dia será {dia[2]}/{dia[1]}/{dia[0]}")


if __name__ == "__main__":
    main()
