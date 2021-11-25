
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM funcao_escolha_chars
import time
def char_ladino():
    time.sleep(2)
    print("\nVocê nunca conheceu sua mãe, mesmo assim a figura materna nunca lhe fez falta pois seu pai su")
    time.sleep(2)

    print("O que você faz?")
    time.sleep(2)
    print("\nOpção 1\n")

    print(("="*20) + (" OU ") + ("="*20))

    time.sleep(5)
    print("\nOpção 2")
    time.sleep(2)

    condicao = True
    while condicao:
        time.sleep(4)
        opcao = input("\n Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")
        if opcao.upper() == "1":
            time.sleep(2)
            print("\n DESCREVA O QUE ACONTECE NA OPÇÃO 1")
            time.sleep(4)
            print("\n DESCREVER O QUE ACONTECE PRA ELE IR PRA TAVERNA ACEITAR A MISSÃO.")
            condicao = False
        elif opcao.upper() == "2":
            time.sleep(2)
            print("\n DESCREVA O QUE ACONTECE NA OPÇÃO 2")
            time.sleep(4)
            print("\n DESCREVER O QUE ACONTECE PRA ELE IR PRA TAVERNA ACEITAR A MISSÃO.")
            condicao = False
        elif opcao.upper() == "S":
            time.sleep(1)
            print(quadrado)
            break
        else:
            time.sleep(1)
            print("\nOpção inválida.")

char_ladino()

