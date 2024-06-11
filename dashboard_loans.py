import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard')

COLUMN_customer_age = 'customer_age'
COLUMN_customer_income = 'customer_income'

#G://11751//pythons//streamlit//banco_de_dados_csv//
DATA_URL = ('./data/LoansDatasest.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

#
data_load_state = st.text('Carregando dados ...')
data = load_data(10000)
data_load_state.text("Dados concluídos!")

if st.checkbox('Exibir tabela de dados'):
    st.subheader('Tabela')
    st.write(data)


#st.subheader('Number of pickups by hour')
#chart_data = pd.DataFrame(x=data[COLUMN_customer_age], y=data[COLUMN_loan_amnt])
#st.line_chart(chart_data)
chart_data = pd.DataFrame(
   {
       "customer_age": data[COLUMN_customer_age],
       "customer_income": data[COLUMN_customer_income],
   }
)

st.bar_chart(chart_data, x="customer_age", y="customer_income")


