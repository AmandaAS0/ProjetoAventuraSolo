
# IMPORTANTE: ESTAS FUNÇÕES SÃO CHAMADAS EM funcao_descricao_desafio_acordar
sorte = 0
import random
import time

def rolagem_desafio_acordar_maga():

    condicao = True
    while condicao:
        print("\nHora do teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
        numero_aleatorio = random.randint(1, 10)
        time.sleep(1)
        sorte = int(input("Escolha um número entre 1 e 10:  "))
        if sorte < 1 or sorte > 10:
            time.sleep(1)
            print("Você digitou uma opção inválida. ")
            condicao = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
            print("\nVocê é acordada com um barulho de passos curtos e um leve cheiro de carniça.  Da foqueira resta uma pequena fagulha que ilumina um mínimo ao seu redor. Próximo a você estão os seus dois companheiros ainda dormindo e vários pares de pequenos olhos vermelhos. Você se levanta no pulo assustando os seus colegas e também as pequenas criaturas. GUERREIRO joga um grande punhado de folhas e galhos secos na fogueira e agora você vê bichos que lembram ratazanas super crescidas. Lhe vem a memória de já ter lido sobre eles e dos problemas que eles costumam causar. Olhando em volta você percebe que LADINO já está empunhando uma rapieira em umas das mãos e uma faca na outra. GUERREIRA está desembanhando a espada. Numa contagem rápida é possível ver 5 deles armados com adagas e prontos pra atacar em torno de vocês. - Kobolds, são kobolds. Você grita e já começa a pensar no feitiço mais efetivo.")

            print(" \nOs Kobolds se posicionam de forma a ficar 2 lutando contra GUERREIRA, 2 contra LADINO e 1 parado a um metro de você.\n")
            from combate_kobolds import combate_kobolds_noite_maga
            condicao = False

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
            print("\nVocê não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("\nVocês foram atacados enquanto dormiam e todos morreram. Foram dormir bêbados, não revezaram a vigilha entre outras falhas que evidenciam o despreparo de vocês como aventureiros emergentes.")
            print("Lamento, mas essa aventura acabou para você...")
            break
            quit()


#==============================================================================================================================

def rolagem_desafio_acordar_ladino():
    contador = True
    while contador:
        print("\nHora do teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
        numero_aleatorio = random.randint(1, 10)
        sorte = int(input("Escolha um número entre 1 e 10:  "))
        if sorte < 1 or sorte > 10:
            print("Você digitou uma opção inválida. ")

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
            print("Eu tirei {} e você {}. Você passou no teste.".format(numero_aleatorio, sorte))
            from combate_kobolds import combate_kobolds_noite_ladino
            contador = False

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print("\nVocês foram atacados enquanto dormiam e todos morreram. Foram dormir bêbados, não revezaram a vigilha entre outras falhas que evidenciam o despreparo de vocês como aventureiros emergentes.")
            print("Lamento, mas essa aventura acabou para você...")
            break
            quit()

#==============================================================================================================================


def rolagem_desafio_acordar_guerreira():
    print("\nHora do teste. Você deverá escolher um número que deverá ser igual ou mais próximo possível da minha escolha com uma variação máxima de 1 pra - ou + ok!?")
    sorte = int(input("Escolha um número entre 1 e 10:  "))

    contador = True
    while contador:
        numero_aleatorio = random.randint(1, 10)
        if sorte < 1 or sorte > 10:
            print("Você digitou uma opção inválida. ")
            contador = False

        elif sorte == numero_aleatorio + 1 or sorte == numero_aleatorio - 1 or sorte == numero_aleatorio:
            from combate_kobolds import combate_kobolds_noite_guerreira
            contador = False

        elif sorte != numero_aleatorio + 1 or sorte != numero_aleatorio - 1 or sorte != numero_aleatorio:
            print("Você não teve tanta sorte assim, eu tirei {} e você {}.".format(numero_aleatorio, sorte))
            print(
                "\nVocês foram atacados enquanto dormiam e todos morreram. Foram dormir bêbados, não revezaram a vigilha entre outras falhas que evidenciam o despreparo de vocês como aventureiros emergentes.")
            print("Lamento, mas essa aventura acabou para você...")
            break
            quit()

rolagem_desafio_acordar_maga()
rolagem_desafio_acordar_ladino()
rolagem_desafio_acordar_guerreira()
