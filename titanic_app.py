import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
import altair as alt

path = "train.data"
df = pd.read_csv(path, index_col= 'PassengerId')
st.title("Streamit Histogramas Titanic")
st.header("Rafael Takata García")
st.dataframe(df.head(3))
st.markdown('## Histogramas por features') 

for feature in df:
    chart_data = df[feature]
    c = (
        alt.chart(chart_data)
        .mark_bar()
        .encode(x = feature)
    )
