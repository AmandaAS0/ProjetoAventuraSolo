
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM aventura_solo_fantasia
opcao_char = 0

def chars_escolha():
    print("\nopção 1. Andhara - Maga... Meio elfa, orfã de pai e mãe, você viveu em um orfanato na região mais pobre do reino.")
    print("\nopção 2. Guíles - Ladino... Halfling, abandonado ainda pequeno pela mãe, você foi criado apenas pelo pai. Sempre teve conforto financeiro mas sabia bem qual era o pagamento por isso por isso.")
    print("\nopção 3. Liene - Guerreira... Humana, princesa herdeira da coroa, presenciou, junto com sua mãe, a morte de seu pai quando tinha 13 anos e junto com ele foram-se os melhores anos de sua vida. ")


    condicao = True
    while condicao:
        opcao_char = input("\nEscolha 1 para jogar com Andhara, 2 para jogar com Ladino, 3 para jogar com Guerreiro ou [S] para sair do jogo:  \n")

        if opcao_char == "1":
            from funcao_andhara import char_mage
            from funcao_encontro_taverna import os_tres_se_encontram
            from funcao_descricao_desafio_acordar import primeiro_desafio_maga
            condicao = False

        elif opcao_char == "2":
            from funcao_ladino import char_ladino
            from funcao_encontro_taverna import os_tres_se_encontram
            from funcao_descricao_desafio_acordar import primeiro_desafio_ladino
            condicao = False

        elif opcao_char == "3":
            from funcao_guerreira import char_guerreira
            from funcao_encontro_taverna import os_tres_se_encontram
            from funcao_descricao_desafio_acordar import primeiro_desafio_guerreira

            condicao = False
        elif opcao_char.upper() == "S":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

chars_escolha()