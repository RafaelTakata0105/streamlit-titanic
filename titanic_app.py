import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

path = "train.data"
df = pd.read_csv(path, index_col= 'PassengerId')
st.title("Streamit Histogramas Titanic")
st.header("Rafael Takata García")
st.dataframe(df.head(3))
st.markdown('## Histogramas por features') 

def graph_creator(dataframe, column):
    data = dataframe[column].value_counts().reset_index()
    data.columns = [column, 'Count']
    chart = alt.Chart(data).mark_bar(color='red').encode(
        x = alt.X(f'{column}:N', title = column),
        y = alt.Y('Count:Q', title = 'Frecuencia'),
)
    st.altair_chart(chart)
   
graph_creator(df, 'Survived')
graph_creator(df, 'Pclass')
graph_creator(df, 'Age')
graph_creator(df, 'SibSp')
graph_creator(df, 'Parch')
graph_creator(df, 'Fare')