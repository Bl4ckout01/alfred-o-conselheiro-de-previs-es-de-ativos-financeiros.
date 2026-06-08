# Alfred - Conselheiro Financeiro

print("Olá! Eu sou o Alfred 🤵📊")
print("Vou analisar tendências básicas para te ajudar.\n")

acoes = {
    "PETR4": [28, 29, 30, 31, 32],
    "VALE3": [70, 69, 68, 67, 66],
    "ITUB4": [25, 25.5, 26, 26.5, 27]
}

print("Analisando ações...\n")

for acao, precos in acoes.items():
    inicio = precos[0]
    fim = precos[-1]

    print(f"Ação: {acao}")

    if fim > inicio:
        print("📈 Tendência de alta")
        print("👉 Pode ser interessante observar para compra\n")

    elif fim < inicio:
        print("📉 Tendência de baixa")
        print("👉 Melhor ter cautela ou esperar\n")

    else:
        print("➡️ Estável")
        print("👉 Sem tendência clara\n")
