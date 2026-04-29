print("""1. À vista(em especie) - 15% de desconto.
2.Cartão de débito - 10% de desconto.
3.Cartão de crédito(vencimento) - 5% de desconto""")

totalvenda = float(input("digite o valor total da venda: "))
pagamento = int(input("Digite a opção de pagamento: "))
if pagamento <1 or pagamento >3:
    print("não tem essa opção")
else:
    if pagamento == 1:
        desconto1 = totalvenda*0.15
        valorfinal = totalvenda - desconto1
        print(f"o valor final é: {valorfinal}")
    elif pagamento == 2:
        desconto2 = totalvenda*0.10
        valorfinal2 = totalvenda - desconto2
        print(f"o valor final é: {valorfinal2}")
    elif pagamento == 3:
        desconto3 = totalvenda*0.05
        valorfinal3 = totalvenda - desconto3
        print(f"o valor final é: {valorfinal3}")
    else:
        print("achou seu valor final")

