from datetime import datetime

from coinbase import consultar_preco
from banco import criar_tabela, inserir_preco
import time

criar_tabela()

moedas = ["BTC-USD",
         "ETH-USD",
         "SOL-USD",

            ]
while True:
    for moeda in moedas:

        dados = consultar_preco(moeda)

        preco = float(dados["data"]["amount"])

        data_hora = datetime.now()

        inserir_preco(moeda, preco, data_hora)

        print("Dados coletados com Sucesso")

        print("Moeda:", moeda)
        print("preço:", preco)
        print("Data e Hora:", data_hora)

    print("Todas as moedas foram coletadas com sucesso!!!")


    time.sleep(60)  # Aguardar 60 segundos antes de coletar novamente
