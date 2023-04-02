cpf = float(input("Informe seu CPF ou CNPJ: "))


print("Opção 1: Solicitar guincho")
print("Opção 2: Falar com atendente")
print("Opção 3: Recomeçar com outro CPF ou CNPJ")

inf = int(input("Informe a opção desejada: "))

match inf:
    case 1:
       print("Para prosseguir precisamos de algumas informações.")
       veic = input("Qual a placa do veiculo: ")
       print("Para te atender melhor, preciso saber o que houve com o veículo.")

       print("Opção 1: Meu veiculo parou e preciso remove-lo do local.")
       print("Opção 2: Acabou o combustivel.")
       print("Opção 3: Meu veiculo está com problema e não sei o motivo.")
       print("Opção 4: Acidente, incendio ou enchente.")
       print("Opção 5: Não encontrei o que preciso.")

       dica = int(input("Dica: digite a informação que mais se adequa a situação: "))

       match dica:
           case 1:
               end = input("Informe o endereço que devemos encaminhar o guincho: ")
               agr = int(input("Digite 1 para atendimento imediato ou 2 para agendamento: "))
               if (agr == 1):
                   print("Aguarde, ja enviamos um guincho até você.")
               elif (agr == 2):
                   agen = input("Para qual data e horario gostaria de agendar? ")
                   print(f"Agendamento feito com sucesso para: {agen}")
               else:
                   print("Opção invalida.")
           case 2:
               end = input("Informe o endereço que devemos encaminhar o guincho: ")
               agr = int(input("Digite 1 para atendimento imediato ou 2 para agendamento: "))
               if (agr == 1):
                   print("Aguarde, ja enviamos um guincho até você.")
               elif (agr == 2):
                   agen = input("Para qual data e horario gostaria de agendar? ")
                   print(f"Agendamento feito com sucesso para: {agen}")
               else:
                   print("Opção invalida.")
           case 3:
               end = input("Informe o endereço que devemos encaminhar o guincho: ")
               agr = int(input("Digite 1 para atendimento imediato ou 2 para agendamento: "))
               if (agr == 1):
                   print("Aguarde, ja enviamos um guincho até você.")
               elif (agr == 2):
                   agen = input("Para qual data e horario gostaria de agendar? ")
                   print(f"Agendamento feito com sucesso para: {agen}")
               else:
                   print("Opção invalida.")
           case 4:
               end = input("Informe o endereço que devemos encaminhar o guincho: ")
               agr = int(input("Digite 1 para atendimento imediato ou 2 para agendamento: "))
               if (agr == 1):
                   print("Aguarde, ja enviamos um guincho até você.")
               elif (agr == 2):
                   agen = input("Para qual data e horario gostaria de agendar? ")
                   print(f"Agendamento feito com sucesso para: {agen}")
               else:
                   print("Opção invalida.")
           case 5:
               print("Aguarde! Iremos te ligar em alguns instantes.")
           case _:
               print("Opção invalida.")

    case 2:
       print("Aguarde que iremos encaminhar para um especialista")
    case 3:
      print("Informe o CPF ou CNPJ: ")
    case 4:
        print("Opção invalida")
