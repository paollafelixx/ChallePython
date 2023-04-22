lista_usuarios = [[60189327044, "EEC6113", "Ricardo"], [96544199044, "FCD4439", "Fernanda"], [39893414059, "DVD2600", "Karla"], [36103280028, "DHW0260", "Ashley"]]

cpf = input ("Digite seu CPF: ")
veic = input("Digite a placa do seu veiculo: ")

cpf_numerico = ""
for caractere in cpf:
    if caractere.isdigit():
        cpf_numerico += caractere


esta_cadastrado = False
for usuario in lista_usuarios:
    if cpf_numerico == str(usuario[0]) and veic == usuario[1]:
        esta_cadastrado = True
        break

if esta_cadastrado:
    print('Você está cadastrado.')
else:
    print('Você não está cadastrado.')