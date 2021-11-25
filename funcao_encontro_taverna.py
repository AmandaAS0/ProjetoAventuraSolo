
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM funcao_escolha_chars
def os_tres_se_encontram():
    print("\nDESCREVER A TAVERNA E A MESA ONDE JÁ SE ENCONTRAM OS OUTROS DOIS E O CONTRATANTE.")
    print("\nVocês três são brevemente apresentados e sem mais delongas ele informa como será a missão. E então, vc está dentro?")

    print("\nOpção 1. Vc aceita?\n")

    print(("=" * 20) + (" OU ") + ("=" * 20))

    print("\nOpção 2. Vc não aceita?")

    condicao = True
    opcao = input("\n Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")

    while condicao:
        if opcao.upper() == "1":
            print("\n Você aceitou a missão. Todos dormirão no mesmo quarto com três camas e partirão para missão ao amanhecer.\n")
            print("\nO dia seguinte inicia-se bem cedo e vocês iniciam a caminhada com todo o equipamento necessário pra sobreviência na floresta e o mapa que deverão seguir se quiserem chegar ao destino.\n")
            condicao = False

        elif opcao.upper() == "2":
            print("\n Você não aceitou a missão. Retorne pra sua casa e siga sua vida.\n")
            condicao = False

        elif opcao.upper() == "S":
            print("\nSaindo do jogo...")
            break

        else:
            print("\nOpção inválida.")

os_tres_se_encontram()


