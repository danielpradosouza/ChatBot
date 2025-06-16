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
           quant_pess=int(input("Para quantas pessoas será o atendimento?"))
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
if tipo_pess==2:
    nome_emp=input("Digite o nome da sua empresa:")
    Cnpj=input("digite seu CNPJ ex:00.000.000/0000-00 : ")
    cep=input("digite seu cep ex: 00000-000 : ")
    espa_audi=int(input("Sua empresa possui um espaço para apresentações? digite 1 para sim e 2 para não"))
    tipo_eve_emp=int(input("Cadastro finalizado com sucesso! Qual dos eventos abaixo melhor atende às suas "
                            "necessidades? digite 1 para Workshop presencial sobre norma NR-1 ,digite 2 para"
                             " Workshop online sobre norma NR-1, digite 3 Palestra presencial e digite 4 para"
                             " Palestra online"))
    if tipo_eve_emp==1:
        quant_pess_emp=int(input("Para quantas pessoas será a apresentação? "))
        print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")
    if tipo_eve_emp==2:
        quant_pess_emp=int(input("Para quantas pessoas será a apresentação? "))
        Apli_emp=int(input("Você prefere usar algum aplicativo específico? Algumas opções: Microsoft "
                          "Teams, Google Meet ou WhatsApp (chamada de vídeo) "
                          "Digite 1 para microsoft Teams, 2 para google meet e 3 para whatsApp"))
        print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")
    if tipo_eve_emp==3:
        Tipo_Pale=input("Sobre qual assunto específico você gostaria que fosse a palestra? (Exemplo:ansiedade, autoestima, etc.)")
        quant_pess_emp=int(input("Para quantas pessoas será a apresentação? "))
        print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!")
    if tipo_eve_emp==4:
       Tipo_Pale=input("Sobre qual assunto específico você gostaria que fosse a palestra? (Exemplo:ansiedade, autoestima, etc.)")
       Apli_emp=int(input("Você prefere usar algum aplicativo específico? Algumas opções: Microsoft "
                          "Teams, Google Meet ou WhatsApp (chamada de vídeo) "
                          "Digite 1 para microsoft Teams, 2 para google meet e 3 para whatsApp"))
       quant_pess_emp=int(input("Para quantas pessoas será a apresentação? "))
       print("Assim que possível a psicóloga Patrícia Marques entrará em contato com você "
                 "para realizar o agendamento. Sua equipe desde já agradece a preferência!") 
