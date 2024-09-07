# Solicitar a idade e a renda mensal do usuário
idade = int(input("Informe sua idade: "))
renda = float(input("Informe sua renda mensal (R$): "))

# Verificar as condições para o empréstimo
if idade < 21:
    print("Idade insuficiente para o empréstimo.")
elif idade > 65:
    print("Idade acima do limite para o empréstimo.")
elif renda < 2000:
    print("Renda insuficiente para o empréstimo.")
else:
    print("Empréstimo aprovado!")
