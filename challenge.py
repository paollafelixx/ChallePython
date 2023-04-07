print("Bem-vindo a NEO Porto. Aqui nos agilizamos seu processo de solicitação de guincho!")
print("")
print("Vamos começar?")
start = int (input("Digite (1) para SIM e (2) para NÃO"))

while start == 1:

    cpf = float(input("Informe seu CPF ou CNPJ: "))
    print("Para prosseguir precisamos de algumas informações.")
    veic = input("Qual a placa do veiculo: ")


#PRIMEIRO VEMOS SE É URGENTE OU NÃO
    imediatouagendamento = int (input("Digite (1) para atendimento imediato ou (2) para agendamento:"))
    match imediatouagendamento:
        case 1:
            print("Atendimento imediato")

            # VEMOS AQUI A SITUACAO

            situacao = int(input("Digite a informação que mais se adequa a situação sendo (1) Acidente de trânsito e (2) falha operacional"))
            match situacao:
                case 1:
                    print("Acidente de trânsito")
                    tipo_carro = int (input("O seu veiuculo é (1) leve/comum ou (2) pesado?"))
                    if tipo_carro == 1: ##carro comum/leve
                        end_leve = input("Qual endereço deveremos ir")
                        tel_leve = input("Qual telefone devemos ligar?")
                        print(f"O guinhco para o veiculo comum/leve de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_leve}")

                    elif tipo_carro == 2:
                        end_pesado = input("Qual endereço deveremos ir")
                        tel_pesado = input("Qual telefone devemos ligar?")

                        guincho_escolha = int (input("Você sabe que tipo de guincho precisaria? (1) - Sim e (2) Não"))
                        if guincho_escolha == 1:
                            tipo_guincho = input("Descreva o tipo de guincho")


                            tipo_guincho = input("Digite o tipo de guinhco que nós encaminharemos para você")
                        elif guincho_escolha == 2:
                            print("Ok, iremos de auxiliar nos próximos passsos")
                            


                            print(f"O guinhco para o veiculo pesado de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_pesado}")
                    else:
                        print("Tipo de carro inválido")





                case 2:
                    print("falha operacional")
        case 2:
            print("Agendamento: OBS: só realizamos agendaentos  dentro do mês de pedido")
            data_agendamento = input("Para qual data gostaria de agendar")
            hora_agendamento = input("Que horas seria feito o atendimento?")
            end_agendamento = input("Qual endereço deveremos ir")
            tel_agendamento = input("Qual telefone devemos ligar?")
            print(f"Seu guinhcho foi agendado para dia {data_agendamento} ás {hora_agendamento} para o endereço {end_agendamento}")
            print("Fim do atendimento")
    break

print("Você desejou não começar")