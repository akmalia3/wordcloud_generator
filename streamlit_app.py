import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.subheader('Wordcloud Generator')
st.write('Enjoy the app 😊')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = pd.read_csv(uploaded_files)
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    st.dataframe(uploaded_file)
