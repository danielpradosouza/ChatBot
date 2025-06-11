nome=input("Digite seu nome:")
idade=int(input("Qual a sua idade?:"))
idade_atual=True
if idade<18:
    idade_atual=False
    print("não trabalhamos com pessoas menores 18 anos")
else:
    idade_atual=True
if idade_atual==True:
    tipo_At=int(input("qual tipo de atendimento voce deseja:" 
                     "1 para empresarial,2 para palestra" 
                     ",3 para casal , 4 para em grupo e "
                        "5 para pessoal"))
    if tipo_At==1:
        presensa=int(input("o atendimento sera presincial ou não:"
                            "digite 1 para prencial e 2 para virtual"))
        if presensa==1:   
            ambiante=(int(input("sua empresa poossui auditorio?: digite "
                            "1 para sim e 2 para não"))) 
            if ambiante==1:
                print("Estou te colocando para "
                     " entrar em contato com a Patricia")
            else:
                print("Tente arrumar um local e" 
                       " entre em contato com a Patricia")                             
        else:
            print("Estou te colocando para "
                     " entrar em contato com a Patricia")
    if tipo_At==2:
        presensa1=(int(input("o atendimento sera presincial ou não:"
                            "digite 1 para prencial e 2 para virtual")))
        if presensa1==1:
            ambiante=(int(input("Voce poossui auditorio?: digite "
                                "1 para sim e 2 para não")))
            if ambiante==1:
                print("Estou te colocando para "
                     " entrar em contato com a Patricia")
            else:
                print("Tente arrumar um local e" 
                       " entre em contato com a Patricia")
        else:
            print("Estou te colocando para "
                     " entrar em contato com a Patricia")
    if tipo_At==3:
        nome_conj=input("Digite o nome do seu Conjuge")
        print("Estou te colocando para entrar em contato com a Patricia pois" 
              "o atendimento será somente virtual")
    if tipo_At==4:
        Num_pessoas=int(input("digite o numero de pessoas que"
                              "vão participar dessa terapia em grupo"))
        print("Estou te colocando para entrar em contato com a Patricia pois" 
              "o atendimento será somente virtual")
    if tipo_At==5:
         print("Estou te colocando para entrar em contato com a Patricia pois" 
              "o atendimento será somente virtual")