import requests

def consultar_preco(moeda):
    url = f"https://api.coinbase.com/api/v2/prices/{moeda}/spot"
    resposta = requests.get(url)

    dados = resposta.json()

    return dados


# try:
#     print("Iniciando Consulta. Aperte Ctrl+c para parar.")
#     while True:
#         print(consultar_preco("BTC-USD"))
#         time.sleep(30)
#    except KeyboardInterrupt:
#     print("Interrompido pelo usuário!")



#moeda_2 = input("Qual a moeda que deseja saber o preço: ex(BTC-USD, ETH-USD,...)")
#print(consultar_preco(moeda_2))
#Apache airflow (Orquestrador de tarefas e rotinas de dados)



#print(input("Digite a moeda a ser consultada!"))
