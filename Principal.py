import streamlit as st
import pandas as pd
import numpy as np
import time
from io import StringIO

#configs
st.set_page_config(
    page_title="Plataforma BI - AzuLab",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Página principal')

#layout do container
with st.sidebar:
    st.write("Boas vindas, @jdgreco!")

    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )
    
    if st.button("Desconectar"):
        st.switch_page("pagesff/page_1.py")