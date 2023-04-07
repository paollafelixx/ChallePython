print("Bem-vindo a NEO Porto. Aqui nos agilizamos seu processo de solicitação de guincho!")
print("")
print("Vamos começar?")
start = int (input("Digite (1) para SIM e (2) para NÃO"))

while start == 1:

    cpf = float(input("Informe seu CPF ou CNPJ: "))
    print("Para prosseguir precisamos de algumas informações.")
    veic = input("Qual a placa do veiculo: ")


            #PRIMEIRO VEMOS SE O ATENTIMENTO É IMEDIATO OU DE AGENDAMENTO
    imediatouagendamento = int (input("Digite (1) para atendimento imediato ou (2) para agendamento:"))
    match imediatouagendamento:
        case 1:
            print("Atendimento imediato")

            #CASO SEJA IMEDIATO, AQUI VEMOS O QUE ACONTECEU 

            situacao = int(input("Digite a informação que mais se adequa a situação sendo (1) Acidente de trânsito e (2) falha operacional"))
            match situacao:
                #SITUAÇÃO 1 - ACIDENTE DE CARRO
                case 1:
                    print("Acidente de trânsito")

                    #AQUI PERGUNTAMOS SE O CARRO QUE SOFREU O ACIDENTE DE TRANSITO É LEVE OU COMUM

                    tipo_carro = int (input("O seu veiuculo é (1) leve/comum ou (2) pesado?"))
                    if tipo_carro == 1:

                        
                            #TRANSITO + LEVE
                         
                            end_leve = input("Qual endereço deveremos ir")
                            tel_leve = input("Qual telefone devemos ligar?")
                            print(f"O guinhco para o veiculo comum/leve de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_leve}")
                            deseja_cont_leve_transito = input("Encerrar atendimento? (1) para SIM e (2) para NÃO")
                            while deseja_cont_leve_transito == 1:
                                print("fim do atentimento")   
                            
                           
                            #TRANSITO + PESADO
                    elif tipo_carro == 2:
                        end_pesado = input("Qual endereço deveremos ir")
                        tel_pesado = input("Qual telefone devemos ligar?")
                            #PERGUNTAMOS SE O DONO DO VEICULO PESADO JÁ TEM CONHECIMENTO DO TIPO DE GUINHCO QUE PRECISA
                        guincho_escolha = int (input("Você sabe que tipo de guincho precisaria? (1) - Sim e (2) Não"))
                            #CASO SIM, NÓS PEDIMOS MAIS INFORMAÇÕES PARA CONFIRMAR E ENVIAMOS.
                        if guincho_escolha == 1:
                            tipo_guincho = input("Digite o tipo de guinhco que nós encaminharemos para você")


                            #CASO NÃO, NÓS PEDIMOS MAIS INFORMAÇÕES.
                        elif guincho_escolha == 2:
                            print("Ok, iremos de auxiliar nos próximos passsos.")
                            #TENTAMOS VER SE O DONO SABE ALGO SOBRE VEICULOS PESADOS PRIMEIRO MAS CASO NÃO, NÓS ENVIAMOS O AUXILIO TAMBÉM
                            print("Digite de acordo com seu conhecimento as seguintes especificações se souber. (Caso não saiba, digite apenas 0 em cada uma")

                            tipo_carroceria = int(input("Digite o tipo de carroceria"))
                            chassi_alongado = int(input("Seu chassi é alongado?"))
                            comprimento = int(input("Qual o comprimento do seu veiculo?"))
                            peso_com_carga = int(input("Peso do veiculo com a carga"))
                            peso_sem_carga = int(input("Peso do veiculo sem a carga"))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo"))

                            #SE O DONO NÃO SOUBER DE NADA, NÓS ENVIAMOS O AUXILIO.
                            if tipo_carroceria and chassi_alongado and comprimento and peso_com_carga and peso_sem_carga and quantidade_de_eixos == 0:
                                print(f"Iremos encaminha um de nossos atendentes para te auxiliar melhor. Confirme os dados abaixo: ")
                                print(f"Guincho pedido pelo CPF/CNPJ: {cpf}")
                                print(f"Ser atendido no endereço: {end_pesado}")
                                print(f"Telefone para contato: {tel_pesado}")
                                confirmacao_pessoa_nao_sabe = int (input("Digi"))
                                print("Você confirma os dados abaixo?")
                                #CONFIRMAÇÃO DE PEDIDO PARA O VEICULO PESADO, CASO O DONO NÃO SOUBER DE NADA
                            print(f"O guinhco para o veiculo pesado de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_pesado}")
                    else:
                        print("Tipo de carro inválido")





                case 2:
                    print("falha operacional")

                    tipo_carro = int (input("O seu veiuculo é (1) leve/comum ou (2) pesado?"))
                    if tipo_carro == 1: 
                            #FALHA + LEVE
                        end_leve = input("Qual endereço deveremos ir")
                        tel_leve = input("Qual telefone devemos ligar?")
                        print(f"O guinhco para o veiculo comum/leve de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_leve}")
                            #FALHA + PESADO
                    elif tipo_carro == 2:
                        end_pesado = input("Qual endereço deveremos ir")
                        tel_pesado = input("Qual telefone devemos ligar?")
                            #PERGUNTAMOS SE O DONO DO VEICULO PESADO JÁ TEM CONHECIMENTO DO TIPO DE GUINHCO QUE PRECISA
                        guincho_escolha = int (input("Você sabe que tipo de guincho precisaria? (1) - Sim e (2) Não"))

                            #CASO SIM, PEDIMOS O MODELO E DETALHES DO VEICULO PARA CONFIRMAR
                        if guincho_escolha == 1:
                            tipo_guincho = input("Digite o tipo de guinhco que nós encaminharemos para você")


                            #CASO NÃO, NÓS PEDIMOS MAIS INFORMAÇÕES.
                        elif guincho_escolha == 2:
                            print("Ok, iremos de auxiliar nos próximos passsos.")

                            #TENTAMOS VER SE O DONO SABE ALGO SOBRE VEICULOS PESADOS PRIMEIRO MAS CASO NÃO, NÓS ENVIAMOS O AUXILIO TAMBÉM

                            print("Digite de acordo com seu conhecimento as seguintes especificações se souber. (Caso não saiba, digite apenas 0 em cada uma")

                            tipo_carroceria = int(input("Digite o tipo de carroceria"))
                            chassi_alongado = int(input("Seu chassi é alongado?"))
                            comprimento = int(input("Qual o comprimento do seu veiculo?"))
                            peso_com_carga = int(input("Peso do veiculo com a carga"))
                            peso_sem_carga = int(input("Peso do veiculo sem a carga"))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo"))

                            #SE O DONO NÃO SOUBER DE NADA, NÓS ENVIAMOS O AUXILIO.
                            if tipo_carroceria and chassi_alongado and comprimento and peso_com_carga and peso_sem_carga and quantidade_de_eixos == 0:
                                print(f"Iremos encaminha um de nossos atendentes para te auxiliar melhor. Confirme os dados abaixo: ")
                                print(f"Guincho pedido pelo CPF/CNPJ: {cpf}")
                                print(f"Ser atendido no endereço: {end_pesado}")
                                print(f"Telefone para contato: {tel_pesado}")
                                confirmacao_pessoa_nao_sabe = int (input("Digi"))
                                print("Você confirma os dados abaixo?")
                                #CONFIRMAÇÃO DE PEDIDO PARA O VEICULO PESADO, CASO O DONO NÃO SOUBER DE NADA
                                print(f"O guinhco para o veiculo pesado de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_pesado}")
                                print("Atendimento encerrado")
                            else:
                                print("Analisaremos as informações e enviaremos o guincho para o")
                    else:
                        print("tipo de carro inválido")

        #CASO AGENDAMENTO        
        case 2:
            print("Agendamento: OBS: só realizamos agendamentos dentro do mês do pedido")
            data_agendamento = input("Para qual data gostaria de agendar")
            hora_agendamento = input("Que horas seria feito o atendimento?")
            end_agendamento = input("Qual endereço deveremos ir")
            tel_agendamento = input("Qual telefone devemos ligar?")
            print(f"Seu guinhcho foi agendado para dia {data_agendamento} ás {hora_agendamento} para o endereço {end_agendamento}")
            print("Fim do atendimento")
    

print("Atendimento encerrado")