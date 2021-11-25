import time

def opcao_inicial():
    print("\nO REINO DE THELOS PRECISA DE AVENTUREIRES COMO VOCÊ.")
    time.sleep(1)
    print("\nPara iniciar o jogo escolha uma das opções.")

    print("[I]niciar o jogo")
    print("[S]air do jogo")
    print("[C]réditos")

    condicao = True
    while condicao:
        opcao = input("Digite a opção:  \n")
        if opcao.upper() == "I":
            time.sleep(1)
            from funcao_prologo_do_mundo import prologo_mundo #FUNÇÃO PROLOGO DO MUNDO
            print("\nApresentamos a você os três personagens desta saga.")
            from funcao_escolha_chars import chars_escolha   # FUNÇÃO ESCOLHA CHARS E APRESENTAÇÃO

            condicao = False
        elif opcao.upper() == "S":
            print("Saindo do jogo...")
            break
        elif opcao.upper() == "C":
            print("CRÉDITOS?")
            condicao = False
        else:
            print("Opção inválida. Escolha um dos 3 personagens ou S para sair.")


opcao_inicial()
