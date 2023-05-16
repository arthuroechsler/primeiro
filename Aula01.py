print("Bem vindo a loja do Arthur luis oechsler")
# dados solicitados para usuario
product_price = float(input("Entre com o preço do produto: "))
product_qtd = float(input("Quantas unidades cliente esta levando?: "))
raw_total = product_price*product_qtd

# calcular descontos na cadeia if else abaixo
if product_qtd <= 9:
    discounted_total = raw_total
elif product_qtd <= 10 and product_qtd < 100:
    discounted_total = raw_total*0.95
elif product_qtd <= 100 and product_qtd < 999:
    discounted_total = raw_total*0.90
else:
    discounted_total = raw_total*0.85
# saida
print("O preço total sem desconto é de: R${:.2f}".format(raw_total))
print("O preço total com desconto é de: R${:.2f}".format(discounted_total))
print("Aluno RU 4344489")
