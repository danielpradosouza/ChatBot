tipo_pess=int(input("Olá! Para melhor te atender, você é uma" 
                    "pessoa física ou uma empresa? digite 1" 
                    "para pessoa fisica e 2 para pessoa juridica"))
if tipo_pess==1:
    nome=input("Digite seu nome:")
    idade=int(input("Qual a sua idade?:"))
    Cpf=input("digite seu CPF ex:000.000.000-00 : ")
    cep=input("digite seu cep ex: 00000-000 : ")
    idade_atual=True
    if idade<18:
        idade_atual=False
        print("não trabalhamos com pessoas menores 18 anos")
    else:
        idade_atual=True
    if idade_atual==True:
        tipo_At=int(input("qual tipo de atendimento voce deseja:" 
                        "1 para em grupo,2 para casal" 
                        ",3 para individual "))
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
