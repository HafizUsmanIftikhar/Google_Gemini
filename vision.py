from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!=None:
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)

    return response.text



st.set_page_config(page_title="Gemini Image Demo 🤖",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Gemini Image Demo 🤖")
input=st.text_input("Input Prompt", key="input")
uploaded_file=st.file_uploader("Choees an Image of Invoice ...", type=["jpg","png","jpeg"])
submit=st.button("Tell me about image")

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

if submit:
    response = get_gemini_response(input,image)
    st.header("The Response is ")
    st.write(response)