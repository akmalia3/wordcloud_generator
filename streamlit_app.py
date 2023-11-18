import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.subheader('Wordcloud Generator')
st.write('Enjoy the app 😊')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write("Filename:", uploaded_file.name)
        st.dataframe(df)

        # Generate Word Cloud
        if st.button('Generate Word Cloud'):
            text_data = ' '.join(df['your_column_name'])  # Replace 'your_column_name' with the actual column containing text data
            wordcloud = WordCloud().generate(text_data)

            # Plot Word Cloud
            plt.figure(figsize=(10, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.pyplot(plt)
