import streamlit as st
import pandas as pd
from plotly import express as px
# Configuração da página
st.set_page_config(page_title="DESPESAS", layout="wide")
# Título da aplicação
st.title("Despesas no Credito")
df= pd.read_csv("parcelado.csv",sep=';',decimal=',')
df_soma = df.sum()
df_soma = df_soma[2:]
df_para_ploty = df_soma.reset_index()
df_para_ploty.columns = ['Meses', 'Valores']  # renomeia colunas
col1,col2 = st.columns(2)
col3,col4 = st.columns(2)
fig = px.bar(df_para_ploty, x='Meses', y='Valores', title='Valores contratados por Mês')
col1.plotly_chart(fig)
col2.dataframe(df_para_ploty,hide_index=True)
df['SET'] = df['SET'].astype(str).str.replace(' ', '').str.replace(',', '.').astype(float)
# Agrupar por 'ITEM' e somar a coluna 'SET'
df_grup = df.groupby('ITEM', as_index=False)['SET'].sum()
df_grup = df_grup.sort_values(by='SET', ascending=False)
fig2 = px.bar(df_grup, x='ITEM', y='SET', title='Itens de mais Gastos')
df_grup['SET']= df_grup['SET'].map(lambda x: f"{x:.2f}")
col3.plotly_chart(fig2)
col4.dataframe(df_grup,hide_index=True)
# item= st.sidebar.selectbox("Item",df['ITEM'].unique())
# df_filtro = df[df['ITEM'] == item]
# df_filtro
# print(df_filtro.sum())
