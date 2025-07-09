print("=== Bem-vindo ao Restaurante===")

nome = input("Por favor, informe seu nome: ")
confirmarNome = input("Você é o responsável pela reserva? ")
quantidade_pessoas = input("Quantas pessoas estarão na reserva? ")
data_reserva = input("Para qual data deseja reservar? (ex: 08/07/2025): ")
horario_reserva = input("Qual horário deseja reservar? (ex: 19:30): ")
email = input("Por favor, digite seu email para confirmar a reserva: ")
mesa = input ("Você deseja assentos preferenciais? (ex: mesa externa, área com ar-condicionado, lugar mais reservado): ")

print(f"Nome: {nome}")
print(f"Número de pessoas: {quantidade_pessoas}")
print(f"Data: {data_reserva}")
print(f"Horário: {horario_reserva}")
print(f"Email para confirmação: {email}")
print(f"Mesa desejada: {mesa}")
print("\n.")

verMenu = int(input("Você deseja ver o menu antecipado? Digite: \n 1-Sim, 2-Não: "))

print("Bebidas: \n 1-coca cola (Preço 12,50 R$)\n 2-guarana (Preço 12,00 R$)\n 3-pepsi (Preço 13,50 R$)\n 4- cerveja atersanal (Preço R$ 27,50 ) \n 5- vinho tinto (Preço 47,90 R$)")
opcao = input("Escolha o número da bebida: ")

if opcao == "1":
    print("Você escolheu Coca-Cola - R$ 12,50")
elif opcao == "2":
    print("Você escolheu Guaraná - R$ 12,00")
elif opcao == "3":
    print("Você escolheu Pepsi - R$ 13,50")
elif opcao == "4":
    print("Você escolheu Cerveja artesanal - R$ 27,50")
elif opcao == "5":
    print("Você escolheu Vinho tinto - R$ 47,90")
else:
    print("Opção inválida.")

print("\n Prato Principal: \n 1- Espaguete ao alho e óleo Preço R$ 24,90)\n 2- Lasanha à bolonhesa (Preço  R$ 34,90)\n 3- Strogonoff de carne/frango (Preço R$ 29,00)")

opcao = input("Escolha o número do prato principal: ")

if opcao == "1":
    print("Você escolheu Espaguete ao alho e óleo - R$ 24,90")
elif opcao == "2":
    print("Você escolheu Lasanha à bolonhesa - R$ 34,90")
elif opcao == "3":
    print("Você escolheu Strogonoff de carne/frango - R$ 29,00")
else:
    print("Opção inválida.")
