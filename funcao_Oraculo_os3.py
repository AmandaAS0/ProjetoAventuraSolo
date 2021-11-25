# ESTAS FUNÇÕES SÃO CHAMADAS EM funcao_combate_segundo_turno_os_tres
import time

def oraculo_maga():

    print("\nVocê e seu grupo adentram a caverna levando a pequena criatura como refém. Ele os guia pelo labirinto de forma a evitar o pequeno grupo de Kobolds que habitam ali. E juntamente com o as indicações do mapa vocês conseguem avançar em seu caminho.\n")

    print("\nAs orientações do mapa são realmente precisas quanto ao caminho que deve ser seguido, mas não informa nada sobre desafios e armadilhas que podem ser encontrados.\n\n Caminhando pelos corredores vocês se deparam com o que parecem bustos de pedra se elevando das paredes. Seis belas esculturas com formas de meias mulheres com seios e cabelos ornamentados com flores e folhas de ouro e no caminho que se segue entre elas ossos e morte. \n\nAs duas primeiras cabeças abrem os olhos e se viram pra vocês, uma de cada lado da parede com olhos brilhando como brasas de uma fogueira. - Aproximem-se aqueles que serão testados. - elas dizem olhando diretamente para vocês. O corredor entre elas é estreito e vocês se posicionam em fila entre as seis cabeças, cada um de você com duas lhes encarando lado a lado. As seis falam em unisono: - Respondam ou morram.")

    condicao = True
    while condicao:
        print("AhA!, agora que o bicho pega. Responda as charadas com uma única palavra.")
        time.sleep(2)
        print("\nMuitos podem ouvi-lo, mas ninguém o pode ver. Se não falarmos, ele também não falará")
        resposta = input("\nEntão, qual é a resposta?  ")

        if resposta.upper() == "ECO": #CHARADA 1
            time.sleep(1)
            print("\nVocês acertaram a primeira charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as segundas cabeças, cujos olhos são tão brancos e frios como o interior de uma geleira, lançam a segunda pergunta.  ")
            time.sleep(2)
            print("\nQuanto maior é, menos se vê:")
            resposta = input("\nEntão, qual é a resposta?  ")

            if resposta.upper() == "SOMBRA": #CHARADA 2
                print("\n\nVocês acertaram a segunda charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as terceiras cabeças, que parecem ter água escaldante e vapor em seus olhos lançam a terceira pergunta.")
                print("\n\nPode ser aberto, mas nunca fechado.")
                resposta = input("\nEntão, qual é a resposta?  ")

                if resposta.upper() == "OVO":  # CHARADA 3
                    time.sleep(1)
                    print("\n\nTodas as seis cabeças falam em conjunto: - Vocês conquistaram o direito de continuar, podem seguir.")
                    from final import final_maga

                else:
                    print("Resposta...")
                    time.sleep(3)
                    print("ERRADA! Vocês são totalmente banhados por ácido, a dor de suas carnes derretendo e pingando como vela dura poucos segundos e todos morrem derretidos.")
                    print("Essa aventura acabou pra vocês...")
                    break
                    quit()

            else:
                print("Resposta...")
                time.sleep(3)
                print("ERRADA! Vocês três recebem uma rajada de gelo e neve de gelar até os ossos e todos morrem congelados. Dia de sorvete para os Kobolds da caverna.")
                print("Essa aventura acabou pra vocês...")
                break
                quit()

        else:
            print("\nResposta...")
            time.sleep(3)
            print("ERRADA! Vocês três recebem um vigoroso jato de fogo e todos morrem queimados. Dia de churrasco para os Kobolds da caverna.")
            print("Essa aventura acabou pra vocês...")
            break
            quit()

#==============================================================================================================================================================

def oraculo_ladino():

    print("\nVocê e seu grupo adentram a caverna levando a pequena criatura como refém. Ele os guia pelo labirinto de forma a evitar o pequeno grupo de Kobolds que habitam ali. E juntamente com o as indicações do mapa vocês conseguem avançar em seu caminho.\n")

    print("\nAs orientações do mapa são realmente precisas quanto ao caminho que deve ser seguido, mas não informa nada sobre desafios e armadilhas que podem ser encontrados.\n\n Caminhando pelos corredores vocês se deparam com o que parecem bustos de pedra se elevando das paredes. Seis belas esculturas com formas de meias mulheres com seios e cabelos ornamentados com flores e folhas de ouro e no caminho que se segue entre elas ossos e morte. \n\nAs duas primeiras cabeças abrem os olhos e se viram pra vocês, uma de cada lado da parede com olhos brilhando como brasas de uma fogueira. - Aproximem-se aqueles que serão testados. - elas dizem olhando diretamente para vocês. O corredor entre elas é estreito e vocês se posicionam em fila entre as seis cabeças, cada um de você com duas lhes encarando lado a lado. As seis falam em unisono: - Respondam ou morram.")

    condicao = True
    while condicao:
        print("AhA!, agora que o bicho pega. Responda as charadas com uma única palavra.")
        time.sleep(2)
        print("\nMuitos podem ouvi-lo, mas ninguém o pode ver. Se não falarmos, ele também não falará")
        resposta = input("\nEntão, qual é a resposta?  ")

        if resposta.upper() == "ECO": #CHARADA 1
            time.sleep(1)
            print("\nVocês acertaram a primeira charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as segundas cabeças, cujos olhos são tão brancos e frios como o interior de uma geleira, lançam a segunda pergunta.  ")
            time.sleep(2)
            print("\nQuanto maior é, menos se vê:")
            resposta = input("\nEntão, qual é a resposta?  ")

            if resposta.upper() == "SOMBRA": #CHARADA 2
                print("\n\nVocês acertaram a segunda charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as terceiras cabeças, que parecem ter água escaldante e vapor em seus olhos lançam a terceira pergunta.")
                print("\n\nPode ser aberto, mas nunca fechado.")
                resposta = input("\nEntão, qual é a resposta?  ")

                if resposta.upper() == "OVO":  # CHARADA 3
                    time.sleep(1)
                    print("\n\nTodas as seis cabeças falam em conjunto: - Vocês conquistaram o direito de continuar, podem seguir.")
                    from final import final_ladino

                else:
                    print("Resposta...")
                    time.sleep(3)
                    print("ERRADA! Vocês são totalmente banhados por ácido, a dor de suas carnes derretendo e pingando como vela dura poucos segundos e todos morrem derretidos.")
                    print("Essa aventura acabou pra vocês...")
                    break
                    quit()

            else:
                print("Resposta...")
                time.sleep(3)
                print("ERRADA! Vocês três recebem uma rajada de gelo e neve de gelar até os ossos e todos morrem congelados. Dia de sorvete para os Kobolds da caverna.")
                print("Essa aventura acabou pra vocês...")
                break
                quit()

        else:
            print("\nResposta...")
            time.sleep(3)
            print("ERRADA! Vocês três recebem um vigoroso jato de fogo e todos morrem queimados. Dia de churrasco para os Kobolds da caverna.")
            print("Essa aventura acabou pra vocês...")
            break
            quit()

#==============================================================================================================================================================

def oraculo_guerreira():

    print("\nVocê e seu grupo adentram a caverna levando a pequena criatura como refém. Ele os guia pelo labirinto de forma a evitar o pequeno grupo de Kobolds que habitam ali. E juntamente com o as indicações do mapa vocês conseguem avançar em seu caminho.\n")

    print("\nAs orientações do mapa são realmente precisas quanto ao caminho que deve ser seguido, mas não informa nada sobre desafios e armadilhas que podem ser encontrados.\n\n Caminhando pelos corredores vocês se deparam com o que parecem bustos de pedra se elevando das paredes. Seis belas esculturas com formas de meias mulheres com seios e cabelos ornamentados com flores e folhas de ouro e no caminho que se segue entre elas ossos e morte. \n\nAs duas primeiras cabeças abrem os olhos e se viram pra vocês, uma de cada lado da parede com olhos brilhando como brasas de uma fogueira. - Aproximem-se aqueles que serão testados. - elas dizem olhando diretamente para vocês. O corredor entre elas é estreito e vocês se posicionam em fila entre as seis cabeças, cada um de você com duas lhes encarando lado a lado. As seis falam em unisono: - Respondam ou morram.")

    condicao = True
    while condicao:
        print("AhA!, agora que o bicho pega. Responda as charadas com uma única palavra.")
        time.sleep(2)
        print("\nMuitos podem ouvi-lo, mas ninguém o pode ver. Se não falarmos, ele também não falará")
        resposta = input("\nEntão, qual é a resposta?  ")

        if resposta.upper() == "ECO": #CHARADA 1
            time.sleep(1)
            print("\nVocês acertaram a primeira charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as segundas cabeças, cujos olhos são tão brancos e frios como o interior de uma geleira, lançam a segunda pergunta.  ")
            time.sleep(2)
            print("\nQuanto maior é, menos se vê:")
            resposta = input("\nEntão, qual é a resposta?  ")

            if resposta.upper() == "SOMBRA": #CHARADA 2
                print("\n\nVocês acertaram a segunda charada, mas logo em seguida as seis cabeças falam novamente juntas: - Respondam ou morram. E as terceiras cabeças, que parecem ter água escaldante e vapor em seus olhos lançam a terceira pergunta.")
                print("\n\nPode ser aberto, mas nunca fechado.")
                resposta = input("\nEntão, qual é a resposta?  ")

                if resposta.upper() == "OVO":  # CHARADA 3
                    time.sleep(1)
                    print("\n\nTodas as seis cabeças falam em conjunto: - Vocês conquistaram o direito de continuar, podem seguir.")
                    from final import final_guerreira

                else:
                    print("Resposta...")
                    time.sleep(3)
                    print("ERRADA! Vocês são totalmente banhados por ácido, a dor de suas carnes derretendo e pingando como vela dura poucos segundos e todos morrem derretidos.")
                    print("Essa aventura acabou pra vocês...")
                    break
                    quit()

            else:
                print("Resposta...")
                time.sleep(3)
                print("ERRADA! Vocês três recebem uma rajada de gelo e neve de gelar até os ossos e todos morrem congelados. Dia de sorvete para os Kobolds da caverna.")
                print("Essa aventura acabou pra vocês...")
                break
                quit()

        else:
            print("\nResposta...")
            time.sleep(3)
            print("ERRADA! Vocês três recebem um vigoroso jato de fogo e todos morrem queimados. Dia de churrasco para os Kobolds da caverna.")
            print("Essa aventura acabou pra vocês...")
            break
            quit()


oraculo_maga()
oraculo_ladino()
oraculo_guerreira()