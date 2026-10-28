# Painel de Criptomoedas — Coinbase

Projeto acadêmico em Python para coletar cotações de Bitcoin (BTC), Ethereum (ETH) e Solana (SOL) em dólares americanos, armazenar os dados em SQLite e visualizar o histórico com Streamlit.

## Funcionalidades

- Consulta de preços spot na API pública da Coinbase.
- Coleta sequencial das três moedas, com pausa de 60 segundos ao final de cada ciclo.
- Armazenamento local de moeda, preço e data/hora da coleta.
- Painel com último preço, variação absoluta entre as duas últimas observações, máximo, mínimo, média e amplitude.
- Seleção de moeda, gráficos de dispersão e linha e tabela de registros.

## Estrutura

| Arquivo | Responsabilidade |
| --- | --- |
| `coinbase.py` | Consulta à API Coinbase |
| `banco.py` | Criação da tabela e inserção de preços |
| `coleta.py` | Execução contínua da coleta |
| `app.py` | Painel Streamlit |
| `requirements.txt` | Dependências diretas nas versões verificadas |

Fluxo: **API Coinbase → coletor Python → SQLite → Streamlit**.

## Como executar no Windows (PowerShell)

Pré-requisitos: Python 3.12, Git e acesso à internet para instalar as dependências e consultar cotações. Os comandos devem ser executados na raiz do projeto.

### 1. Baixar e instalar

```powershell
git clone https://github.com/laerciosantanadda-hash/coinbase1.git
cd coinbase1
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Crie o ambiente virtual no próprio computador; não copie o ambiente de outro PC. Não é necessário ativá-lo para usar os comandos abaixo.

### 2. Iniciar a coleta

No primeiro terminal:

```powershell
.\.venv\Scripts\python.exe coleta.py
```

Aguarde a confirmação de coleta das três moedas. O arquivo `coinbase.db` será criado automaticamente. Para encerrar a coleta, pressione `Ctrl+C`.

### 3. Abrir o painel

Em outro terminal, entre na mesma pasta do projeto e execute:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Acesse o endereço exibido no terminal, normalmente http://localhost:8501. O painel pode ser utilizado com o histórico já salvo mesmo depois de interromper o coletor.

## Observações e limitações

- O banco é gerado localmente e não acompanha o repositório; execute o coletor antes de abrir o painel pela primeira vez.
- Execute os dois processos na mesma pasta, pois o caminho do banco é relativo.
- Os valores são em USD e as datas usam o relógio local do computador, sem informação de fuso armazenada.
- Os indicadores consideram todo o histórico disponível da moeda selecionada. A variação exibida não representa necessariamente uma variação diária.
- O cache do painel dura 60 segundos, mas não provoca atualização automática da tela. Após esse intervalo, recarregue a página ou interaja com o painel para consultar os dados novamente.
- O coletor ainda não implementa tempo limite, tratamento de falhas da API ou novas tentativas automáticas. Uma falha pode interromper a execução.
- O projeto consulta cotações; não realiza ordens de compra ou venda.

## Verificação realizada

O painel foi executado com `streamlit.testing.v1.AppTest`, com o banco local existente: três indicadores de moeda, sem exceções nem mensagens de erro. Isso não substitui a verificação da conectividade com a API no computador de destino.
