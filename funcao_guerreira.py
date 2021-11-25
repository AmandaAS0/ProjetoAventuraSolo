
# IMPORTANTE: ESTA FUNÇÃO É CHAMADA EM funcao_escolha_chars

import time
def char_guerreira():
    time.sleep(2)
    print("\n\nLiene, você é a primeira de seu nome. Embora você provenha de gerações e gerações de monarcas, seu altruísmo e compaixão diferem de grande parte da sua família. Mesmo não tendo mais a figura paterna desde a adolescência, você ainda carrega consigo as melhores lembranças e ensinamentos que pôde aprender e isso inclui a sua paixão por armas. Após a sua morte, não tardou para que você começasse a se dedidar as espadas. E essa dedicação à arte que seu pai tanto amava foi o único acalento que você conseguiu obter já que sua mãe parecia não sentir a perda.")
    print("\n\n Hoje é mais uma noite insone onde você dá voltas pela cama sem conseguir dormir. Isso se repete com frequência desde a morte do seu pai e hoje você resolveu andar pelos corredores do castelo procurando pelo seu sono. \n Vagando pelos corredores e observando as tapeçarias nas paredes, você escuta um murmúrio vindo do quarto de sua mãe. Você aproxima-se devagar, e pela fechadura da porta é possível ver um homem atravessando o quarto e sua mãe logo em seguida, ambos estão completamente nús e sua mãe está grávida. \n\n Todas as teorias possíveis passam rapidamente pela sua cabeça onde a mais revoltante delas é que, em seu leito de morte, seu pai jamais soube da vinda de uma futura criança. \n\n O luto sequer acabou, a cama sequer esfriou, e ao conjecturar uma suposta traíção, seu espanto e repulsa liberam um arquejar tão audível que parece ter atraído a atenção dos que estavam no quarto. Você escuta algo sendo murmurado e passos pesados na direção da porta.")
    time.sleep(2)

    print("\nO que você faz?\n")
    time.sleep(2)
    print("\nApressa-se para encontrar um lugar onde possa se esconder para que não descubram que você estava bisbilhotando.\n")

    print(("="*20) + (" OU ") + ("="*20))

    time.sleep(2)
    print("\nEspera que alguém abra a porta para que você possa ficar cara a cara com esse ato tão repulsivo")
    time.sleep(2)


    condicao = True
    while condicao:  # NECESSÁRIO CRIAR UMA CONDIÇÃO DE PARADA PRA SAIR DO LOOP ETERNO
        opcao = input("\n Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")
        if opcao.upper() == "1":
            print("\n Você se escondeu, e equanto tenta conter o soluço e as lágrias, consegue escutar sua mãe falando pra alguém dentro do quarto que não havia motivo para ter medo. Não havia ninguém ali e provavelmente foi apenas o vento.\n\n   Ao retornar para o seu quarto você é consumida pelo choro e pela dor da traição póstuma. A certeza que aquela barriga não provem de seu pai lhe deixa temerosa quanto ao futuro de tudo. Agora mais do que nunca você deve aprender, aprimorar e trabalhar para proteger o seu legado e o seu povo. ")
            condicao = False
        elif opcao.upper() == "2":
            print("\n Mesmo sentindo o tremor nos joelhos e o suor na testa, você se mantém firme, a porta é aberta, sua mãe aparece completamente nua e antes de falar qualquer coisa você recebe uma bofetada que lhe joga pro chão. Esse é o momento em que sua mãe lhe coloca no seu lugar, ela é a rainha e você apenas uma criança tola capaz de inventar coisas. A porta se fecha na sua cara enquanto você tenta conter o soluço e as lágrimas. \n\n   Ao retornar para o seu quarto você é consumida pelo choro e pela dor da traição póstuma. A certeza que aquela barriga não provem de seu pai lhe deixa temerosa quanto ao futuro de tudo. Agora mais do que nunca você deve aprender, aprimorar e trabalhar para proteger o seu legado e o seu povo. ")
            print("\n\nOs anos foram passando, anos de muito treino, muito empenho e esmero. Você se tornou uma bela moça e não lhe faltam pretendentes. Ainda mais agora que a notícia da doença de sua mãe começa a se espalhar entre os súditos. Você recebe uma convocação para um encontro particular com sua mãe e o conselheiro e nesse encontro lhe transmitida a missão para salvar a vida da rainha. Ela confia em você, na sua determinação e na sua nobreza para ser curada. Tudo que você precisa pra dar início a sua aventura já está pronto e você partirá em algumas horas.")
            condicao = False
        elif opcao.upper() == "S":
            print("Saindo do jogo...")
            break
        else:
            print("\nOpção inválida.")
    #       opcao = input("\n Se você escolheu a Opção 1 então digite [1], se escolheu a Opção 2 então digite [2]. Digite [S] para sair do jogo: ")

char_guerreira()