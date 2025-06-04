nome=input("Digite seu nome:")
idade=int(input("Qual a sua idade?:"))
if idade<18:
    print("não trabalhamos com pessoas menores 18 anos")
else:
    tipo_At=int(input("qual tipo de atendimento voce deseja:" 
                    "1 para empresarial,2 para palestra" 
                    ",3 para casal , 4 para em grupo e "
                        "5 para pessoal"))
    if tipo_At==1:
        presensa=int(input("o atendimento sera presincial ou não:"
                            "digite 1 para prencial e 2 para virtual"))
        if presensa==1:   
                ambiante=(input("sua empresa poossui auditorio?: digite "
                                "1 para sim e 2 para não")) 
                if ambiante==1:
                     print("Estou te colocando para "
                         "  entrar em contato com a Patricia")
                else:
                     print("Tente arrumar um local e" 
                           " entre em contato com a Patricia")
             
        else:
            print("Estou te colocando para "
                         "  entrar em contato com a Patricia")