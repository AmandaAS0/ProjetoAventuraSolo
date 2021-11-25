#IMPORTANTE: ESTAS FUNÇÕES SÃO CHAMADAS EM combate_kobolds.

import time
import random


def combate_maga_segundo_turno():
    condicao = True
    while condicao:
        print("\nMais um teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?\n")
        numero_aleatorio = random.randint(1, 10)
        time.sleep(1)
        sorte = int(input("Escolha um número entre 1 e 10:  "))

        if sorte < 1 or sorte > 10:
            time.sleep(1)
            print("Você digitou uma opção inválida. ")
            condicao = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:  # SE PASSOU NO TESTE:
            print(" \n\nUm virote é lançado de algum lugar escuro da floresta a sua volta e passa zumbindo no seu ouvido, olhando ao redor você consegue ver o par de olhos vermelhos que ataca da escuridão. Mirando fixamente entre os olhos do Kobold você começa a conjuração de uma nova magia enquanto LADINO, desviando de um golpe que seria dado pelas costas, vira-se pra pequena criatura e desfere um ataque perfurante direto no olho esquerdo do oponente. GUERREIRA com sua espada ainda em mãos gira todo o seu corpo e sua espada vorpal separando cabeça e corpo da ratazana gigante. Antes que sua magia seja lançada, o Kobold sai das sombras com os braços abertos e desarmado. Para surpresa de todos do grupo o Kobold fala a sua lingua, oferece rendição e ajuda pois ele conhece muito bem os arredores da floresta.\n")
            from funcao_Oraculo_os3 import oraculo # TEXTO IGUAL PARA OS 3


        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:  # SE NÃO PASSOU NO TESTE:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("NÃO PASSOU!  No momento que LADINO se volta para o oponente em suas costas, um virote vindo de algum lugar escuro da floresta entra o pescoço dele com tanta força que o leva imediatamente para o chão dando ao Kobold que estava em suas costas a chance de deferir o ataque final. Tamanha atrocidade faz com que você perca a concentração da magia que estava invocando e quando dá por sí, você a dor lascinante de uma faca adentrando suas entranhas. Sua ultima visão é de duas dessas criaturas cercando GUERRREIRA e uma terceira saindo da floresta com uma besta apontada pra cabeça dela.\n\n")

    print("Lamento, mas essa aventura acabou pra você...")
    quit() #FORÇA A SAIR DO CÓD SE DER GAMEOVER


#==============================================================================================================================

def combate_ladino_segundo_turno():
    condicao = True
    while condicao:
        print("Mais um do teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
        numero_aleatorio = random.randint(1, 10)
        time.sleep(1)
        sorte = int(input("Escolha um número entre 1 e 10:  "))

        if sorte < 1 or sorte > 10:
            time.sleep(1)
            print("Você digitou uma opção inválida. ")
            condicao = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:  # SE PASSOU NO TESTE:
            print("\n Um virote é lançado de algum lugar escuro da floresta a sua volta e passa zumbindo no seu ouvido, olhando ao redor um par de olhos vermelhos denuncia de onde estava vindo o ataque. GUERREIRA com sua espada já em mãos gira seu troco e pernas junto com sua espada vorpal separando cabeça e tronco da ratazana gigante. Você mira sua adaga bem no meio dos olhos vermelhos e instantes antes de lança-la o Kobold sai das sombras com os braços abertos e desarmado. Para surpresa de todos do grupo, ele vem falando sua lingua, oferece rendição e ajuda pois ele conhece muito bem os arredores da floresta. ")
            from funcao_Oraculo_os3 import oraculo # TEXTO IGUAL PARA OS 3
            from final import final_ladino #FINAL INDIVIDUAL COM DUAS ESCOLHAS

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:  # SE NÃO PASSOU NO TESTE:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("NÃO PASSOU!  No momento que você se volta para o oponente em suas costas, um virote vindo de algum lugar escuro da floresta atravessa seu pescoço com tanta força que o leva imediatamente para o chão dando ao Kobold que estava em suas costas a chance de deferir o ataque final. você sente a dor lascinante de uma faca adentrando suas entranhas. Sua ultima visão é da GUERREIRA com a garganta corta de lado a lado e você escuta logo atrás de você os gritos agonizantes de Andhara.\n\n")

            print("Lamento, mas essa aventura acabou pra você...")
            quit() # FORÇA A SAIR DO CÓD SE DER GAMEOVER

#==============================================================================================================================

def combate_guerreira_segundo_turno():
    condicao = True
    while condicao:
        print(
            "Mais um teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
        numero_aleatorio = random.randint(1, 10)
        time.sleep(1)
        sorte = int(input("Escolha um número entre 1 e 10:  "))

        if sorte < 1 or sorte > 10:
            time.sleep(1)
            print("Você digitou uma opção inválida. ")
            condicao = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:  # SE PASSOU NO TESTE:
            print("\n Um virote é lançado de algum lugar escuro da floresta a sua volta e passa zumbindo no seu ouvido, olhando ao redor um par de olhos vermelhos denuncia de onde estava vindo o ataque. Com sua espada ainda em mãos gira seu troco e pernas junto com sua espada vorpal separando cabeça e tronco da ratazana gigante próxima de você. LADINA mira sua adaga bem no meio dos olhos vermelhos e instantes antes de lança-la o Kobold sai das sombras com os braços abertos e desarmado. Para surpresa de todos do grupo, ele vem falando sua lingua, oferece rendição e ajuda pois ele conhece muito bem os arredores da floresta. ")
            from funcao_Oraculo_os3 import oraculo # TEXTO IGUAL PARA OS 3
            from final import final_guerreira #FINAL INDIVIDUAL COM DUAS ESCOLHAS

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:  # SE NÃO PASSOU NO TESTE:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("NÃO PASSOU!  No momento que você se volta para o oponente em suas costas, um virote vindo de algum lugar escuro da floresta atravessa seu pescoço com tanta força que o leva imediatamente para o chão dando ao Kobold que estava em suas costas a chance de deferir o ataque final. você sente a dor lascinante de uma faca adentrando suas entranhas. Sua ultima visão é da GUERREIRA com a garganta corta de lado a lado e você escuta logo atrás de você os gritos agonizantes de Andhara.\n\n")

            print("Lamento, mas essa aventura acabou pra você...")
            quit()  # FORÇA A SAIR DO CÓD SE DER GAMEOVER

combate_maga_segundo_turno()
#combate_ladino_segundo_turno()
#combate_guerreira_segundo_turno()
