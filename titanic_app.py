import streamlit as st
import pandas as pd
import matplotlib as plt
path = "train.data"
df = pd.read_csv(path, index_col= 'PassengerId')
st.title("Streamit Histogramas Titanic")
st.header("Rafael Takata García")
st.dataframe(df.head(3))
st.markdown('## Histogramas por features') 
st.altair_chart(df.hist(figsize=[7,7], xlabelsize=5))
st.markdown('### Survived')
st.altair_chart(df['Survived'].plot(kind='hist', bins = 2, edgecolor = "BLACK"))
st.markdown('### Passenger class')
st.altair_chart(df['Pclass'].plot(kind='hist', bins = 3, color="#F2AB6D", edgecolor = "BLACK"))
st.markdown('### Age')
st.altair_chart(df['Age'].plot(kind='hist', edgecolor = "WHITE", bins= 8))
st.markdown('### Siblings/Spouses aboard')
st.altair_chart(df['SibSp'].plot(kind='hist', legend=True, bins=8))
st.markdown('### Parents/children aboard')
st.altair_chart(df['Parch'].plot(kind='hist', grid= True, xlabel="Parents / children aboard", bins = 6))
st.markdown('### Passenger fare')
st.altair_chart(df['Fare'].plot(kind='hist', grid=True, edgecolor="BLACK", bins = 5))
