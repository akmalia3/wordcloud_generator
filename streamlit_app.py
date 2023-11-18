import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader('Wordcloud Generator')
st.write('Enter your text below and click the button to generate a Word Cloud 😊')

# Text input box
user_input = st.text_area("Enter your text here:", "")

# Generate Word Cloud
if st.button('Generate Word Cloud'):
    if user_input:
        wordcloud = WordCloud().generate(user_input)

        # Plot Word Cloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
    else:
        st.warning("Please enter some text to generate a Word Cloud.")
