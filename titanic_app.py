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
   
st.markdown('### Survived')  
graph_creator(df, 'Survived')
st.markdown('### Passenger class')  
graph_creator(df, 'Pclass')
st.markdown('### Age')  
graph_creator(df, 'Age')
st.markdown('### Sibling or spouses aboard')  
graph_creator(df, 'SibSp')
st.markdown('### Parents and children aboard')  
graph_creator(df, 'Parch')
st.markdown('### Ticket Fare')  
graph_creator(df, 'Fare')
