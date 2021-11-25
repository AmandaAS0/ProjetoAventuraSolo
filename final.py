
import time
# IMPORTANTE: ESTAS FUNÇÕE SÃO CHAMADAS EM funcao_Oraculo_os3
# ESCOLHA DOS FINAIS. SÃO DOIS FINAIS DIFERENTES PRA CADA PERSONAGEM.


def final_maga():
    time.sleep(2)
    print("\n   De fato não foi fácil, mas vocês chegaram até aqui, passaram por desafios, tiveram que fazer escolhas. Mas nenhuma das escolhas feitas anteriormente foi tão difícil quando a que terá que fazer agora. E já saíba, de antemão, que nesta história não existe: E eles viveram felizes para sempre...")
    time.sleep(3)
    print("  \nDeixando o pavor e todas aquelas cabeças pra trás , vocês caminham mais um pouco pelos túneis rochosos e a medida que avançam uma iluminação parece vir do fim do túnel. Este ultimo corredor acaba numa cavena bastante ampla, de teto alto de onde um raio de luz amarela como o sol desce por uma fenda bem no topo iluminando uma única flor no centro de um pequeno gramado. A umidade das paredes vira vapor com o calor acumulado peças paredes fazendo toda essa visão parecer um sonho levemente enevoado. \n	Você se aproxima da flor e a toca. Sua mente é invadida por imagens, visões e flashs. Tudo em sequencia desconexa como se fossem lembranças do futuro. ")

    time.sleep(2)

    condicao = True
    while condicao:
        print("Existem dois finais para sua trajetória, em ambos você terá de lhe dar com a sua conciência. \n\nOpção 1: você destroi a flor; ===== OU ==== Opção 2: você leva a flor pra concluir a sua missão.")

        time.sleep(2)
        final = input("\n\n Escolha uma das opções: ")

        if final.upper() == "1":
            time.sleep(2)
            print("\n\nSua consciência com o futuro fala mais alto e você pensa que ao destruir esta flor você poderá dar a outras crianças órfãs um futuro melhor. Não apenas de aprender as artes da magia, mas também de aprender o que é ser cuidado, o que é ter uma família e o que é ter amor. Não levar a flor para ele é certamente a melhor coisa a se fazer. \n  Não tarda para que você esteja aos pés do leito de morte do seu instrutor onde um misto de peso e alívio permeia sua consciência. Esta morte você carregará para sempre em suas mãos para que outras dezenas de vidas tenham chances melhores.")
            condicao = False

        elif final.upper() == "2":
            time.sleep(2)
            print("Ao tocar na flor pensamentos vem a sua mente, um flash de inúmeras imagens quase como uma lembrança do futuro. \n Ao mantê-lo vivo você terá a oportunidade de aprender cada vez mais tendo a chance de se superar e superar até mesmo aquele que a educou. O poder adquirido será sua maior recompensa por esta escolha.")
            condicao = False

        else:
            print("Opção inválida, escolha entre 1 ou 2.")

#==============================================================================================================================

def final_ladino():
    time.sleep(2)
    print("\n   De fato não foi fácil, mas vocês chegaram até aqui, passaram por desafios, tiveram que fazer escolhas. Mas nenhuma das escolhas feitas anteriormente foi tão difícil quando a que terá que fazer agora. E já saíba, de antemão, que nesta história não existe: E eles viveram felizes para sempre...")

    time.sleep(2)
    print("  Deixando o pavor e todas aquelas cabeças pra trás , vocês caminham mais um pouco pelos túneis rochosos e a medida que avançam uma iluminação parece vir do fim do túnel. Este ultimo corredor acaba numa cavena bastante ampla, de teto alto de onde um raio de luz amarela como o sol desce por uma fenda bem no topo iluminando uma única flor no centro de um pequeno gramado. A umidade das paredes vira vapor com o calor acumulado peças paredes fazendo toda essa visão parecer um sonho levemente enevoado. \n	Você se aproxima da flor e a toca. Sua mente é invadida por imagens, visões e flashs. Tudo em sequencia desconexa como se fossem lembranças do futuro. ")

    time.sleep(2)

    condicao = True
    while condicao:
        print("\nExistem dois finais para sua trajetória, em ambos você terá de lhe dar com a sua conciência. \n\nOpção 1: você destroi a flor; ===== OU ==== Opção 2: você leva a flor pra concluir a sua missão.")

        time.sleep(2)
        final = input("\n\n Escolha uma das opções: ")

        condicao = True
        if final.upper() == "1":
            time.sleep(1)
            print("FINAL 1.")
            condicao = False


        elif final.upper() == "2":
            time.sleep(2)
            print("FINAL 2")
            condicao = False
            break
        else:
            print("Opção inválida, escolha entre 1 ou 2.")

#==============================================================================================================================

def final_guerreira():
    time.sleep(2)
    print("   De fato não foi fácil, mas vocês chegaram até aqui, passaram por desafios, tiveram que fazer escolhas. Mas nenhuma das escolhas feitas anteriormente será tão difícil quando a que terão que fazer agora. E já saíba, de antemão, que não existe o: E eles viveram felizes para sempre...")

    time.sleep(2)
    print("  Deixando o pavor e todas aquelas cabeças pra trás , vocês caminham mais um pouco pelos túneis rochosos e a medida que avançam uma iluminação parece vir do fim do túnel. Este ultimo corredor acaba numa cavena bastante ampla, de teto alto de onde um raio de luz amarela como o sol desce por uma fenda bem no topo iluminando uma única flor no centro de um pequeno gramado. A umidade das paredes vira vapor com o calor acumulado peças paredes fazendo toda essa visão parecer um sonho levemente enevoado. \n	Você se aproxima da flor e a toca. Sua mente é invadida por imagens, visões e flashs. Tudo em sequencia desconexa como se fossem lembranças do futuro. ")

    time.sleep(2)

    condicao = True
    while condicao:
        print("\nExistem dois finais para sua trajetória, em ambos você terá de lhe dar com a sua conciência. \n\nOpção 1: você destroi a flor; ===== OU ==== Opção 2: você leva a flor pra concluir a sua missão.")

        time.sleep(2)
        final = input("\n\n Escolha uma das opções: ")

        if final.upper() == "1":
            time.sleep(1)
            print("Sua consciência com o todo fala mais alto e você se pergunta? Qual é o custo de uma única vida? Manter sua mãe viva certamente implicará na miséria, morte, colapso do reino e o completo caos pra milhares de pessoas. Ela acreditará na sua nobreza e lealdade e jamais pensará que você está mentindo. Não levar a flor para ela é certamente a melhor coisa a se fazer. \n Não tarda para que você esteja aos pés do leito de morte da sua mãe onde um misto de peso e alívio permeia sua consciência. Esta morte você carregará para toda vida, mas outras milhares serão salvas")
            condicao = False

        elif final.upper() == "2":
            time.sleep(2)
            print("Ao tocar na flor pensamentos vem a sua mente, um flash de inúmeras imagens quase como uma lembrança do futuro. \nManter sua mãe viva certamente implicará na miséria, morte, colapso do reino e o completo caos pra milhares de pessoas. Mas onde estaria sua lealdade e sua nobreza se sua missão não fosse cumprida? \nLevar a flor para ela é certamente a coisa certa a se fazer. Sua mãe ganha algo como a vida eterna e com isso o reino mergulha em séculos de pobreza, fome, doenças e incontáveis mortes.")
            condicao = False

        else:
            print("Opção inválida, escolha entre 1 ou 2.")




final_maga()
final_ladino()
final_guerreira()
