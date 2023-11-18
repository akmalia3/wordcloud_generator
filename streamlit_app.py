import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader('Wordcloud Generator')
st.write('Enjoy the app 😊')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write("Filename:", uploaded_file.name)
        st.dataframe(df)

        # Get the first text column for Word Cloud generation
        text_columns = [col for col in df.columns if df[col].dtype == 'object']
        if not text_columns:
            st.warning("No text columns found in the CSV file.")
        else:
            selected_column = st.selectbox("Select a text column for Word Cloud", text_columns)
            text_data = ' '.join(df[selected_column])

            # Generate Word Cloud
            if st.button('Generate Word Cloud'):
                wordcloud = WordCloud().generate(text_data)

                # Plot Word Cloud
                plt.figure(figsize=(10, 6))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                st.pyplot(plt)
