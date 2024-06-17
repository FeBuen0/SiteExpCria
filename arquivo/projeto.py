prod = [
    {"id": 1, "nome": "Coca-cola", "valor": 3.75, "estoque": 2},
    {"id": 2, "nome": "Pepsi", "valor": 3.67, "estoque": 5},
    {"id": 3, "nome": "Monster", "valor": 9.96, "estoque": 1},
    {"id": 4, "nome": "Café", "valor": 1.25, "estoque": 100},
    {"id": 5, "nome": "Redbull", "valor": 13.99, "estoque": 2},
]

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

def mostrar_produtos():
    print("Produtos disponíveis:")
    for produto in prod:
        print(f"{produto['id']}: {produto['nome']} - R$ {produto['valor']} - Estoque: {produto['estoque']}")

def validar_escolha(escolha):
    for produto in prod:
        if produto["id"] == escolha and produto["estoque"] > 0:
            return produto
    return None

def calcular_troco(troco):
    troco_dict = {}
    for valor in notas:
        if troco >= valor:
            quantidade = int(troco // valor)
            troco = round(troco - quantidade * valor, 2)
            if quantidade > 0:
                troco_dict[valor] = quantidade
    return troco, troco_dict

def comprar_bebida():
    mostrar_produtos()
    escolha = int(input("Escolha o código da bebida desejada: "))
    produto = validar_escolha(escolha)
    if produto:
        print(f"Você escolheu {produto['nome']} que custa R$ {produto['valor']}.")
        valor_pago = float(input("Insira o valor pago: "))
        while valor_pago < produto['valor']:
            print(f"Valor insuficiente. O {produto['nome']} custa R$ {produto['valor']}.")
            valor_pago += float(input("Insira um valor adicional: "))
        troco, troco_dict = calcular_troco(round(valor_pago - produto['valor'], 2))
        if troco == 0:
            print("Seu troco:")
            for valor, quantidade in troco_dict.items():
                print(f"{quantidade} x R$ {valor:.2f}")
            produto['estoque'] -= 1
            print(f"Obrigado por comprar {produto['nome']}!")
        else:
            print("Seu troco:")
            for valor, quantidade in troco_dict.items():
                print(f"{quantidade} x R$ {valor:.2f}")
            produto['estoque'] -= 1
            print(f"Obrigado por comprar {produto['nome']}!")
    else:
        print("Código inválido ou produto fora de estoque.")


while True:
    comprar_bebida()