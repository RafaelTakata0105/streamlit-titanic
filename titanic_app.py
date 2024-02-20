import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np

path = "train.data"
df = pd.read_csv(path, index_col= 'PassengerId')
st.title("Streamit Histogramas Titanic")
st.header("Rafael Takata García")
st.dataframe(df.head(3))
st.markdown('## Histogramas por features') 
st.write(df.hist(figsize=[7,7], xlabelsize=5))
st.markdown('### Survived')
st.write(df['Survived'].plot(kind='hist', bins = 2, edgecolor = "BLACK"))
st.markdown('### Passenger class')
st.write(df['Pclass'].plot(kind='hist', bins = 3, color="#F2AB6D", edgecolor = "BLACK"))
st.markdown('### Age')
st.write(df['Age'].plot(kind='hist', edgecolor = "WHITE", bins= 8))
st.markdown('### Siblings/Spouses aboard')
st.write(df['SibSp'].plot(kind='hist', legend=True, bins=8))
st.markdown('### Parents/children aboard')
st.write(df['Parch'].plot(kind='hist', grid= True, xlabel="Parents / children aboard", bins = 6))
st.markdown('### Passenger fare')
st.write(df['Fare'].plot(kind='hist', grid=True, edgecolor="BLACK", bins = 5))
