import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Dashboard-Coinbase", page_icon="$", layout="wide")

st.title("Painel de Visualização de Criptomoedas")

st.write("Este painel permite visualizar os preços das criptomoedas coletados da API Coinbase e armazenados em um banco de dados SQLite.")

st.write("Visualização dos dados coletados da API Coinbase")

@st.cache_data(ttl=60)

def carregar_dados():
    conexao = sqlite3.connect("coinbase.db")
    try:
        df = pd.read_sql_query("SELECT moeda, preco, data_hora FROM precos ORDER BY data_hora",conexao,)

    finally:
        conexao.close()
    df["data_hora"] = pd.to_datetime(df["data_hora"])
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

    return df


try:

    df = carregar_dados()
except Exception as erro:
    st.error(f"Não foi possível ler o banco de dados: {erro}")
    st.stop()
if df.empty:
    st.warning("Ainda não existem dados no banco.")
    st.stop()


#--------------------- A partir desta linha começa a parte de visualização dos dados -------------------------#

moedas = df["moeda"].unique() # Aqui retorna os três tipos de moedas que estão no banco de dados, ou seja, BTC, ETH e SOL ------------------------#

for coluna, moeda in zip(st.columns(len(moedas)), moedas):
    precos = df.loc[df["moeda"] == moeda, "preco"]

    atual = precos.iloc[-1]
    anterior = precos.iloc[-2] if len(precos) > 1 else None
    delta = f"{atual - anterior:.2f}" if anterior is not None else None



    with coluna:
        st.metric(moeda,f"${atual:.2f}", delta=delta)
        st.write(f"Maior preço: ${precos.max():.2f}")
        st.write(f"Menor preço: ${precos.min():.2f}")
        st.write(f"Preço médio: ${precos.mean():.2f}")
        st.write(f"Amplitude dos preços: ${precos.max() - precos.min():.2f}")

st.divider()

#------------Análises detalhadas--------------------#
st.subheader("Análises da Criptomoeda")

moeda_selecionada = st.selectbox("Selecione a criptomoeda desejada para análise:", moedas)


dados_moeda = df[df["moeda"] == moeda_selecionada]


st.subheader(f"Histórico de preços da {moeda_selecionada}")

st.scatter_chart(dados_moeda.set_index("data_hora")["preco"])
st.line_chart(dados_moeda.set_index("data_hora")["preco"])


st.divider()

st.subheader(f"Dados Coletados da {moeda_selecionada}")

st.dataframe(dados_moeda)
