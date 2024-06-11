#https://docs.streamlit.io/develop/api-reference/connections
#https://docs.streamlit.io/develop/tutorials/multipage/st.page_link-nav

import streamlit as st
import pandas as pd
import numpy as np
import time
from io import StringIO

#configs
st.set_page_config(
    page_title="Relatórios T4R",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Dashboard')

#G://11751//pythons//streamlit//banco_de_dados_csv//

@st.cache_data
def load_data(file_rel, nrows):
    data = pd.read_csv(file_rel, nrows=nrows, delimiter='\"')
    return data

#
# Inicio do relatorio
#
#
data_load_state = st.text('Carregando dados ...')

data_relatorio_1 = load_data('./data/relatorio-2.csv', None)
data_load_state.text("Dados concluídos!")

# processando informacoes
lista_periodos_x = [
    "01/2024", "02/2024", "03/2024", "04/2024",	"05/2024", "06/2024"
]

dicionario_peridos_valores = {}

dicionario_peridos_valores = data_relatorio_1.filter(lista_periodos_x)
dicionario_peridos_valores = dicionario_peridos_valores.iloc[:-1 , :] #remove ultima linha

print(dicionario_peridos_valores)


#chart_data = pd.DataFrame(x=data[COLUMN_customer_age], y=data[COLUMN_loan_amnt])
#st.line_chart(chart_data)

#print(dicionario_peridos_valores.to_numpy())

#somar todos os valores por periodo
def gerarEixoY(dicionario):
    retornoDict = []    
    for valor in dicionario:        
        array = np.nan_to_num(dicionario[valor].values, nan=0.0)
        total = np.sum(array)
        retornoDict.append(total)

    return retornoDict


#layout do container

#with st.sidebar:
#    st.success("Done!")
#    if st.button("Home"):
#       st.switch_page("pagesff/page_1.py")

layout_col1, layout_col2 = st.columns(2)

with layout_col1:
    st.subheader('#1 - Horas por Projetos')

    uploaded_file = st.file_uploader("1")
    if uploaded_file is not None:
        with st.spinner("Loading..."):
            # processando informacoes
            lista_periodos_x = [
                "01/2024", "02/2024", "03/2024", "04/2024",	"05/2024", "06/2024"
            ]

            data_file_upload = load_data(uploaded_file, None)

            dicionario_peridos_valores = {}
            dicionario_peridos_valores = data_file_upload.filter(lista_periodos_x)
            dicionario_peridos_valores = dicionario_peridos_valores.iloc[:-1 , :] #remove ultima linha

            lista_valores_periodos_y = gerarEixoY(dicionario_peridos_valores)

            chart_data = pd.DataFrame(
                {
                    "eixo_x": lista_periodos_x,
                    "eixo_y": lista_valores_periodos_y
                }
            )        

            #componente de exibir tabela de dados no html
            if st.checkbox('Exibir tabela de dados'):
                st.subheader('Tabela')
                st.dataframe(dicionario_peridos_valores, use_container_width=True)

            st.bar_chart(chart_data, x="eixo_x", y="eixo_y")

with layout_col2:
    st.subheader('#1 - Horas por Projetos')

    uploaded_file = st.file_uploader("2")
    if uploaded_file is not None:
        with st.spinner("Loading..."):
            # processando informacoes
            lista_periodos_x = [
                "01/2024", "02/2024", "03/2024", "04/2024",	"05/2024", "06/2024"
            ]

            data_file_upload = load_data(uploaded_file, None)

            dicionario_peridos_valores = {}
            dicionario_peridos_valores = data_file_upload.filter(lista_periodos_x)
            dicionario_peridos_valores = dicionario_peridos_valores.iloc[:-1 , :] #remove ultima linha

            lista_valores_periodos_y = gerarEixoY(dicionario_peridos_valores)

            chart_data = pd.DataFrame(
                {
                    "eixo_x": lista_periodos_x,
                    "eixo_y": lista_valores_periodos_y
                }
            )        

            #componente de exibir tabela de dados no html
            if st.checkbox('Exibir tabela de dados 1'):
                st.subheader('Tabela')
                st.write(dicionario_peridos_valores)

            st.bar_chart(chart_data, x="eixo_x", y="eixo_y")



