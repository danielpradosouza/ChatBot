tipo_pess=int(input("Olá! Para melhor te atender, você é uma " 
                    "pessoa física ou uma empresa? digite 1 " 
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
                        "1 para em grupo,2 para casal " 
                        "e 3 para individual "))
        if tipo_At==1:
           qunat_pess=int(input("Para quantas pessoas será o atendimento?"))
           Apli=int(input("Você prefere usar algum aplicativo específico? Algumas opções: Microsoft "
                          "Teams, Google Meet ou WhatsApp (chamada de vídeo) "
                          "Digite 1 para microsoft Teams, 2 para google meet e 3 para whatsApp"))
           atendi=int(input("Como você gostaria de organizar o atendimento?"
                            "digite 1 para uma sessão específica, 2 para Acompanhamento semanal "
                            "e 3 para Acompanhamento mensal"))
           print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")
        if tipo_At==2:
            nome_conj=input("Digite o nome do seu Conjuge")
            atendi=int(input("Como você gostaria de organizar o atendimento?"
                            "digite 1 para uma sessão específica, 2 para Acompanhamento semanal "
                            "e 3 para Acompanhamento mensal"))
            print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")
        if tipo_At==3:
           atendi=int(input("Como você gostaria de organizar o atendimento?"
                            "digite 1 para uma sessão específica, 2 para Acompanhamento semanal "
                            "e 3 para Acompanhamento mensal"))
           print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")