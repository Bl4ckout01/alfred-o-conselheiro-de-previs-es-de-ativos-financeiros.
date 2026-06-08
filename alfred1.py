#!pip install yfinance pandas scikit-learn jobli

import yfinance as yf
import pandas as pd
from sklearn.linear_model import SGDClassifier

# Escolher ativo
ativo = input("Digite o ativo: ")

# 1. Coletar dados
dados = yf.download(ativo, period="30d", interval="1h")

if dados.empty:
    print("Erro ao baixar dados")
else:
    # 2. Criar indicadores
    dados['retorno'] = dados['Close'].pct_change()
    dados['media_curta'] = dados['Close'].rolling(5).mean()
    dados['media_longa'] = dados['Close'].rolling(20).mean()

    dados = dados.dropna()

    # 3. Criar alvo (1 = sobe, 0 = cai)
    dados['alvo'] = (dados['Close'].shift(-1) > dados['Close']).astype(int)

    # 4. Separar X e y
    X = dados[['retorno', 'media_curta', 'media_longa']]
    y = dados['alvo']

    # 5. Criar modelo
    modelo = SGDClassifier(loss='log_loss')

    # 6. Treinar modelo
    modelo.fit(X, y)

    # 7. Fazer previsão com o último dado
    ultima = X.iloc[-1].values.reshape(1, -1)
    previsao = modelo.predict(ultima)[0]

    # 8. Mostrar resultado
    print("\n===== RESULTADO =====")
    print("Ativo:", ativo)

    if previsao == 1:
        print("📈 Vai subir (talvez)")
    else:
        print("📉 Vai cair (talvez)")
