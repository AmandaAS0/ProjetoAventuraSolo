
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM funcao_escolha_chars
import time
def char_ladino():
    time.sleep(2)
    print("\nVocê nunca conheceu sua mãe, mesmo assim a figura materna nunca lhe fez falta pois seu pai sua mãe, mesmo assim a figura materna nunca lhe fez falta pois seu pai supre tudo que você necessita. Ele lhe dá afeto, cuidados e conforto. Você é tudo pra ele e ele é o seu heroi. \n Mesmo com suas ausências as vezes por dias seguidos, quando volta sempre lhe trás um largo sorriso, histórias de lugaers longínquos e algum souvenir.\n E ainda com todo esse empenho e amor, as vezes você tem a impressão que uma névoa de segredos paira no ar.")
    print("\nCaminhando pelos cômodos da casa você vê a porta do escritório entreaberta e escuta a conversa entre seu pai e um humano que as vezes o visitava. Falavam sobre uma emboscada, como ela seria feita e aonde. Distraidamente você esbarra num vaso, derruba-o e quebra ele por inteiro. O seu pai e o estranho imediatamente vão até a porta, e enquanto você está ajoelhado recolhendo os cacos do chão seu pai lhe pergunta: - Você está aí a muito tempo?")
    time.sleep(2)

    print("O que você faz?")
    time.sleep(2)
    print("\nVocê mente e diz que estava apenas passando e esbarrou.\n")

    print(("="*20) + (" OU ") + ("="*20))

    time.sleep(5)
    print("\nVocê o encara seriamente, não contem sua curiosidade e pergunta sobre o que estavam falando?")
    time.sleep(2)

    condicao = True
    while condicao:
        time.sleep(4)
        opcao = input("\n Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")
        if opcao.upper() == "1":
            time.sleep(2)
            print("\n Você recolhe os pedaços do vaso, joga-os no lixo e vai pra sua cama pensar sobre o que ouviu.")
            time.sleep(2)
            print("\n Anos se passaram e ao longo deles você foi aperfeiçoando suas técnicas. A cerca de dois dias a coisa mais estranha que você jamais pensou aconteceu. Seu pai retornou, mas não era exatamente o seu pai, e sim uma criatura que mudava constantemente de forma. Uma hora halflin, outra hora goblin, as vezes um meio elfo meio halfling, as vezes uma mini harpia com pés de haltling. Todas as combinações de espécies e criaturas pareciam possíveis dentro do tamanho de sua própria raça.")
            time.sleep(3)
            print("\n A única semelhança imutável entre todos as formas era o tapa-olho. O item mágico que possibilitava a variedade de aparências era também um item amaldiçoado já que, uma vez colocado, nem ninguém nesse mundo poderia retirá-lo.")
            time.sleep(3)
            print("\n Finalmente depois de tantos anos chegou o momento de saber. Seu pai fazia parte da guilda dos ladrões da cidade e era lá, e apenas lá que ele poderia pedir algum auxílio pra tal situação. Com as explicações detalhadas do seu pai você conseguiu localizar o local onde os ladinos se escondiam. O líder da guilda lhe informa que conhece alguém que pode retirar o tapa olho amaldiçoado de seu pai mas pra isso precisará de um item tão raro quanto. Você se propões a fazer o que for necessário, toda as informações lhe são passadas e você vai se encaminhando pra saída do local quando um coro de choro estridente lhe chama a atenção, você se direciona ao local, puxa uma cortina e vê em um grande salão uma dúzia de bebês sendo cuidados e amamentados por diversas mulheres e por uma porta do outro lado um homem entra trazendo mais uma criança. Inúmeras questões percorrem a sua cabeça e todas levam aos recentes boatos dos filhos desaparecidos de camponeses.")
            time.sleep(4)
            print("\n A cena tornou-se ainda menos perturbadora que a própria realidade. Você um dia foi um deles, um dos bebês sequestrados, adotado por um integrante da guilda dos ladrões e que a anos assumi a identidade de seu pai. \n\n Partir numa aventura certamente não é a escolha ideal a ser feita nesse momento, mas ficar nesta casa com o homem que mentiu pra você durante toda a sua vida também não é.")
            condicao = False
        elif opcao.upper() == "2":
            time.sleep(2)
            print("\n Seu pai responde o seu olhar com uma simples afirmação. - Você ainda não tem idade pra isso, quando crescer conversaremos mais sobre o mundo, enquanto isso tudo que você precisa fazer é continuar seu estudo e seus treinos. Ele lhe faz um carinho na cabeça, entra novamente no escritório e fecha a porta. Você recolhe os pedaços do vaso, joga-os no lixo e vai pra sua cama pensar sobre o que aconteceu.")
            time.sleep(2)
            print("\n Anos se passaram e ao longo deles você foi aperfeiçoando suas técnicas. A cerca de dois dias a coisa mais estranha que você jamais pensou aconteceu. Seu pai retornou, mas não era exatamente o seu pai, e sim uma criatura que mudava constantemente de forma. Uma hora halflin, outra hora goblin, as vezes um meio elfo meio halfling, as vezes uma mini harpia com pés de haltling. Todas as combinações de espécies e criaturas pareciam possíveis dentro do tamanho de sua própria raça.")
            time.sleep(3)
            print("\n A única semelhança imutável entre todos as formas era o tapa-olho. O item mágico que possibilitava a variedade de aparências era também um item amaldiçoado já que, uma vez colocado, nem ninguém nesse mundo poderia retirá-lo.")
            time.sleep(3)
            print("\n Finalmente depois de tantos anos chegou o momento de saber. Seu pai fazia parte da guilda dos ladrões da cidade e era lá, e apenas lá que ele poderia pedir algum auxílio pra tal situação. Com as explicações detalhadas do seu pai você conseguiu localizar o local onde os ladinos se escondiam. O líder da guilda lhe informa que conhece alguém que pode retirar o tapa olho amaldiçoado de seu pai mas pra isso precisará de um item tão raro quanto. Você se propões a fazer o que for necessário, toda as informações lhe são passadas e você vai se encaminhando pra saída do local quando um coro de choro estridente lhe chama a atenção, você se direciona ao local, puxa uma cortina e vê em um grande salão uma dúzia de bebês sendo cuidados e amamentados por diversas mulheres e por uma porta do outro lado um homem entra trazendo mais uma criança. Inúmeras questões percorrem a sua cabeça e todas levam aos recentes boatos dos filhos desaparecidos de camponeses.")
            time.sleep(4)
            print("\n A cena tornou-se ainda menos perturbadora que a própria realidade. Você um dia foi um deles, um dos bebês sequestrados, adotado por um integrante da guilda dos ladrões e que a anos assumi a identidade de seu pai. \n\n Partir numa aventura certamente não é a escolha ideal a ser feita nesse momento, mas ficar nesta casa com o homem que mentiu pra você durante toda a sua vida também não é.")
            condicao = False
        elif opcao.upper() == "S":
            time.sleep(1)
            print(quadrado)
            break
        else:
            time.sleep(1)
            print("\nOpção inválida.")

char_ladino()

