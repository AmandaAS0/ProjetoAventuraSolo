# IMPORTANTE: ESSAS FUNÇÕES SÃO CHAMADAS EM funcao_rolagem_acordar

import time
import random

def combate_kobolds_noite_maga(): # OBS: TURNO 1 - COMBATE DOIS TURNOS. UMA ROLAGEM DE DADOS POR TURNO.
    print("\nVocê é acordada com um barulho de passos curtos e um leve cheiro de carniça.  Da foqueira resta uma pequena fagulha que ilumina um mínimo ao seu redor. Próximo a você estão os seus dois companheiros ainda dormindo e vários pares de pequenos olhos vermelhos. Você se levanta no pulo assustando os seus colegas e também as pequenas criaturas. GUERREIRO joga um grande punhado de folhas e galhos secos na fogueira e agora você vê bichos que lembram ratazanas super crescidas. Lhe vem a memória de já ter lido sobre eles e dos problemas que eles costumam causar. Olhando em volta você percebe que LADINO já está empunhando uma rapieira em umas das mãos e uma faca na outra. GUERREIRA está desembanhando a espada. Numa contagem rápida é possível ver 5 deles armados com adagas e prontos pra atacar em torno de vocês. - Kobolds, são kobolds. Você grita e já começa a pensar no feitiço mais efetivo.")

    print(" \nOs Kobolds se posicionam de forma a ficar 2 lutando contra GUERREIRA, 2 contra LADINO e 1 parado a um metro de você.")

    condicao = True
    while condicao:
        print("\n Novamente você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
        numero_aleatorio = random.randint(1, 10)
        time.sleep(1)
        sorte = int(input("Escolha um número entre 1 e 10:  "))
        if sorte < 1 or sorte > 10:
            time.sleep(1)
            print("Você digitou uma opção inválida. ")
            condicao = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
            print("VOCÊ PASSOU! Enquanto LADINO crava a rapieira na barriga de um dos dois Kobolds que o cercava, Liene saca a espada no mesmo momento em que um Kobold se lança sobre ela, recebendo nas costelas todo o impacto e indo cair a alguns metros de distância. Você concentra-se na magia que deseja fazer, as palavras vão sendo ditas juntamente com os movimentos manuais que devem ser realizados. A energia necessária é extraída de tudo que lhe rodeia, trabalhada, manipulada e transformada em várias pequenas bolotas de luz branca que são lançadas na direção da criatura a sua frente. Ao tocar no corpo a criatura é imediatamente eletrocutada e cai esfumaçando.")
            from funcao_combate_segundo_turno_os_tres import combate_maga_segundo_turno
            condicao = False

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("\nNÃO PASSOU: Enquanto LADINO direciona sua atenção para o Kobold que está a sua frente, um outro lhe apunhala pelas costas, a lâmina da faca entra completamente e você LADINO caindo de joelhos. Além dele um Kobold está agarrado no pescoço de GUERREIRA cortando sua garganta de um lado ao outro. E mesmo com toda essa barbarie acontecendo a sua volta, você concentra-se na magia que deseja fazer, as palavras vão sendo ditas juntamente com os movimentos manuais que devem ser realizados. A energia necessária é extraída de tudo que lhe rodeia, trabalhada, manipulada e transformada em várias pequenas bolotas de luz branca que são lançadas na direção da criatura a sua frente. Ao tocar no corpo a criatura é imediatamente eletrocutada e cai esfumaçando. Nesse momento você sente uma forte fisgada no coração, um virote de besta acertou seu peito e a dor faz suas pernas fraquejarem. Sua visão vai escurecendo enquanto seu corpo vai caíndo e em meio a penumbra da morte sua útima visão é daquele pequeno diabrete se aproximando com uma faca nas mãos.")
            print("Lamento, mas essa aventura acabou para você...")
            break
            quit()


#========================================================================================================================================================================

# OBS: TURNO 1 - COMBATE DOIS TURNOS. UMA ROLAGEM DE DADOS POR TURNO.
def combate_kobolds_noite_ladino():

    print("\nLADINO Vocé é acordado com um barulho de passos curtos e um leve cheiro de carniça. Da fogueira resta uma pequena fagulha que ilumina um minimo ao seu redor. Próximo a você estão seus dois companheiros ainda dormindo e em volta de vocês vários pares de pequenos olhos vermelhos. Você lse levanta no pulo assustando os seus colegas e também as pequenas criaturas. Andhara joga um grande punhado de folhas e galhos secos da fogueira pra atiçar o fogo e agora você vê os bichos que lembram ratazanas super crescidas. lhe vem a memória de já ter lido sobre eles e dos problrmas que eles costumam causar. Olhando em volta você percebe que GUERREIRA já está sacando a espada e Andhara começa a fazer movimentos com as mãos preparando uma magia. Numa contagem rápida é possível ver em torno de vocês, 5 criaturas armadas com adagas e prontas pra atacar. - KOBOLDS, SÃO KOBOLDS. Você grita e puxa rapidamente sua rapieira e uma faca.\n")

    print("\nOs Kobolds se posicionam de forma a ficar 2 lutando contra GUERREIRA, 2 lutando contra você e o outro próximo de Andhara.")

condicao = True
while condicao:
    print("\n Novamente você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
    numero_aleatorio = random.randint(1, 10)
    time.sleep(1)
    sorte = int(input("Escolha um número entre 1 e 10:  "))
    if sorte < 1 or sorte > 10:
        time.sleep(1)
        print("Você digitou uma opção inválida. ")
        condicao = False

    elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
        print("PASSOU! Você crava sua rapieira na barriga de um dos dois Kobolds que o cercavam e a empurra com o máximo de sua força sentindo toda a resistência das entranhas la dentro. GUERREIRA saca a espada no mesmo momento em que um Kobold se lança sobre ela recebendo nas costelas todo o impacto e indo parar a metros de distância. MAGA lança pequenas orbs d luz que tocam o corpo do Kobold e o eletrocura imediatamente.\n")
        from funcao_combate_segundo_turno_os_tres import combate_ladino_segundo_turno
        condicao = False

    elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
        print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
        print("\n NÃO PASSOU! Enquanto você direciona sua atenção para o Kobold a sua frente, um outro lhe apunhala pelas costas, você sente a lamina entrando e abrindo suas entranhas, cai de joelhos a tempo de sentir uma forte fisgada no coração. Sua visão vai escurecendo e enquanto seu corpo vai caindo ainda é possível ver que um Kobold está agarrado no pescoço de GUERREIRA cortando sua garganta de um lado ao outro. A última coisa que você ouve são os gritos da maga que estava logo atrás de você.\n\n")
        print("Lamento, mas essa aventura acabou para você...")
        break
        quit() # FORÇA A SAIR DO CÓD SE DER GAMEOVER

#========================================================================================================================================================================

def combate_kobolds_noite_guerreira(): # OBS: TURNO 1 - COMBATE DOIS TURNOS. UMA ROLAGEM DE DADOS POR TURNO.
    print("Você é acordada com um barulho de passos curtos e um leve cheiro de carniça.  Da foqueira resta uma pequena fagulha que ilumina um mínimo ao seu redor. Próximo a você estão os seus dois companheiros ainda dormindo e vários pares de pequenos olhos vermelhos. Você se levanta no pulo assustando os seus colegas e também as pequenas criaturas. LADINO joga um grande punhado de folhas e galhos secos na fogueira e agora você vê bichos que lembram ratazanas super crescidas. Lhe vem a memória de já ter lido sobre eles e dos problemas que eles costumam causar. Olhando em volta você percebe que MAGA já está preparando uma magia. LADINO está desembanhando uma rapieira. Numa contagem rápida é possível ver 5 deles armados com adagas e prontos pra atacar em torno de vocês. - Kobolds, são kobolds. Você grita e já começa a pensar no feitiço mais efetivo.")

print(" Os Kobolds se posicionam de forma a ficar 2 lutando contra você, 2 contra LADINO e 1 parado a um metro da MAGA.")

condicao = True
while condicao:
    print("\n Novamente você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
    numero_aleatorio = random.randint(1, 10)
    time.sleep(1)
    sorte = int(input("\nEscolha um número entre 1 e 10:  "))
    if sorte < 1 or sorte > 10:
        time.sleep(1)
        print("\nVocê digitou uma opção inválida. ")
        condicao = False

    elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
        time.sleep(1)
        print("\nPASSOU! No exateo momento em que você saca a sua espada, um dos Kobolds pula na sua direção e você o acerta nas costelas lançando ele a alguns metros de você. LADINO crava sua rapieira na barriga de um dos dois Kobolds que o cercavam e a empurra com o máximo de sua força sentindo toda a resistência das entranhas la dentro. MAGA lança pequenas orbs d luz que tocam o corpo do Kobold e o eletrocura imediatamente.\n")
        from funcao_combate_segundo_turno_os_tres import combate_guerreira_segundo_turno
        condicao = False

    elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
        time.sleep(1)
        print("\nVocê não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
        print("\n NÃO PASSOU! Enquanto você direciona sua atenção para o Kobold a sua frente, um outro pula nas suas costas, você sente a lamina entrando e abrindo sua garganta de um lado a outro e o sangue quente escorrendo por dentro da sua armadura. Sua visão vai escurecendo e enquanto seu corpo vai caindo ainda é possível LADINO sendo apunhalado pelas costas e um virote de besta atravessando o coração de Andhara.\n\n")
        print("Lamento, mas essa aventura acabou para você...")
        break
        quit() # FORÇA A SAIR DO CÓD SE DER GAMEOVER


combate_kobolds_noite_maga()
combate_kobolds_noite_ladino()
combate_kobolds_noite_guerreira()