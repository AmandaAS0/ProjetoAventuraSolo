
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM funcao_escolha_chars
import time
# SE ESCOLHEU OPÇÃO_CHAR 1:
def char_mage(): # Apresentação de personagem 1 e prologo.
    print("\nANDHARA - APRENDIZ DE MAGIA. \n Você é uma jovem orfã chamada Andhara que cresceu em um dos piores orfanatos da cidade de Thelos. Sua aparência franzina torna a sua experiência ainda pior pois dentro dos muros que cercam o prédio, rege a lei do mais forte. Hoje é mais um dia em que você está escondida das outras crianças no pequeno bosque que existe atrás do orfanato. As copas das árvores fazem uma sombra no local onde você está escondida e apesar disso, ao olhar em volta algo lhe chama a atenção. Algo que provavelmente esteve enterrado mas que as recentes chuvas devem ter exposto. \n")
    time.sleep(25)
    print("\n O que você faz?: ")
    time.sleep(2)
    print("\nOpção 1. Você se esgueira em silêncio para que as outras crianças não te ouçam, remexe e escava a terra em volta do objeto. Ao fazer isso você nota que é um pote de barro fechado com uma tampa que pode ser facilmente removida. Ao retirar a tampa, percebe que a sombra das árvores não lhe deixa ver o que lá dentro, você exita um pouco mas sua grande curiosidade faz com que coloque a mão dentro do pote.\n")


    print(("="*20) + (" OU ") + ("="*20))

    time.sleep(22)
    print("\nOpção 2. Você se esgueira em silêncio para que as outras crianças não te ouçam, remexe e escava a terra em volta do objeto. Ao fazer isso você nota que o objeto é um pote de barro fechado com uma tampa que pode ser facilmente removida. Você retira a tampa e percebe que a sombra das árvores não lhe deixa ver o que lá dentro, você pondera que pode haver algo lá dentro que possa lhe machucar. Então calcula que no pico do dia o sol estará mais forte e será possível ver o que tem lá dentro, então fecha a tampa, cobre com terra novamente e volta para o seu esconderijo.\n")


# VAR = PRA ESCOLHER POR A MÃO NO POTE OU NÃO POR A MÃO NO POTE.
    condicao = True
    while condicao:
        opcao_pote = input("Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")
        if opcao_pote == "1":
            print("      " + "\nVOCE ESCOLHEU A OPÇÃO 1. \nVocê retira um grande rolo de papel que parece conter diversos pergaminhos. Escolhe um deles e apesar da lingua estranha a qual nunca teve contato, você percebe que consegue lê-lo. Num deles está escrito transformar em porco, uma serie de linhas escritas e bem no final da página uma palavra escrita em vermelho brilhante e que não faz sentido algum. No exato momento em que você está lendo a estranha palavra, uma das crianças a encontra e lhe agarra pelos cabelos. Ainda sim a pronuncia é concluída, a palavra brilha com grande intensidade, o garoto solta seus cabelos e caindo de quatro no chão, começa a grunhir enquanto seu nariz vai se transformando em um saliente e redondo focinho de porto. As outras três crianças que estavam com ele chegam a tempo de vê-lo com orelhas de porco crescendo acima da cabeça, as calças esticando e rasgando pra dar espaço a um grande lombo com um rabinho rosqueado, e em volta de toda aquela costelinha, bacon, panceta e picanha suina, brilha uma aura vermelha na mesma cor do pergaminho que está em suas mãos. As crianças saem correndo aos gritos e instantes depois uma das cuidadoras do orfanato retira o papel da sua mão, lhe pega pelo braço e leva você pra uma sala onde você espera sentada por um tempo que parece não ter fim. \n")
            time.sleep(25)
            print("      " + "Finalmente você escuta passos e vozes de duas pessoas conversando. Uma delas é a superiora do orfanato e a outra é a voz de um homem que não lhe é familiar. A porta finalmente se abre, ambos entram na sala e param em pé de frente pra voce. A superiora lhe apresenta o Lorde Beltror, o mago oficial do reino. Suas vestes e aparencia impositiva eram realmente marcantes, mas o que mais lhe chama a atenção é sua feição mal humorada e rabugenta. Enquanto você observava o aspecto daquele homem a sua frente, a superiora dava pra ele o pote desenterrado e a autorização escrita para que você fosse com ele.")
            condicao = False
        elif opcao_pote == "2":
            print("\nVOCE ESCOLHEU A OPÇÃO 2. \n Você guardou o pote pra ler depois e retornou ao seu esconderijo. Nesse momento uma das crianças a encontra agarra ela pelos cabelos antes mesmo que ela consiga correr, os outros chegam em seguida trazendo pequenas bolotas de lama que vão sendo arremessadas em você. É até dificil saber o que lhe doi mais: se são as bolotas, as risadas ou as ofensas. Salva pelo gongo, todos param a cruel brincadeira quando toca o sino da refeição e se encaminham cada um pro seu lugar a mesa. Chegando por ultimo e completamente enlameada você é impedida de sentar na mesa com as outras crianças. Seu prato é servido em um canto da sala com a cuidadora dizendo que porco deve comer no chiqueiro. Depois de alimentada, finalmente limpa e com as roupas devidamente trocadas você finalmente dorme.  \n" + "   " + "O dia seguinte começa com um sol radiante e quente e que lhe traria uma intensa paz se não fosse pelo sorriso maldoso das outras crianças. É chegada a hora do sol a pino e vc retorna até o local onde encontrou o seu tesouro. Desenterra e destampa o pote e vê papeis enrolados. Você retira um grande rolo de papel que parece conter diversos pergaminhos. Escolhe um deles e apesar da lingua estranha a qual nunca teve contato, você percebe que consegue lê-lo. Num deles está escrito transformar em porco, uma série de frases e bem no final da página uma palavra escrita em vermelho brilhante e que não faz sentido algum. Sem esperar, alguém chega por trás de você e num único golpe lhe joga pro chão, ainda sim a pronuncia é concluída, a palavra brilha com grande intensidade e você que o garoto que lhe agrediu cai de quatro no chão, começa a grunhir enquanto seu nariz vai se transformando em um saliente e redondo focinho de porto. As outras três crianças que estavam com ele chegam a tempo de vê-lo com orelhas rosadas e pontudas crescendo acima da cabeça, as calças esticando e rasgando pra dar espaço a um grande lombo com um rabinho rosqueado, e em volta de toda aquela costelinha, bacon, panceta e picanha suina, brilha uma aura vermelha na mesma cor do pergaminho que está em suas mãos. As crianças saem correndo aos gritos e instantes depois uma das cuidadoras do orfanato retira o papel da sua mão, lhe pega pelo braço e leva você pra uma sala onde você espera sentada por um tempo que parece não ter fim. \n" + "      " + "Finalmente você escuta passos e vozes de duas pessoas conversando. Uma delas é a superiora do orfanato e a outra é a voz de um homem que não lhe é familiar. A porta finalmente se abre, ambos entram na sala e param em pé de frente pra voce. A superiora lhe apresenta o Lorde Beltror, o mago oficial do reino. Suas vestes e aparencia impositiva eram realmente marcantes, mas o que mais lhe chama a atenção é sua feição mal humorada e rabugenta. Enquanto você observava o aspecto daquele homem a sua frente, a superiora dava pra ele o pote desenterrado e a autorização escrita para que você fosse com ele.\n")
            time.sleep(27)
            print("Seu treinamento é arduo mas sua evolução é impressionantemente rápida. Você cresceu, aprendeu e evoluiu com o custo de muito suor, muitas lágrimas e algumas cicatrizes permanentes. O seu mestre um dia lhe surpreende convidando-a para sentar-se com ele e compartilhar um vinho. Ele está doente, ele vai morrer e sua educação não será completada. Ele é, sem dúvida, um carrasco rabugento mas é também um mago poderoso que está disposto a lhe ensinar muito mais. E é com esse pensamento que você sai em busca de um ítem que poderá fazê-lo viver por mais tempo, pelo menos o tempo de você conseguir dele todo o conhecimento que ele deve ter.  ")



            condicao = False

        elif opcao_pote.upper() == "S":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")


char_mage()
