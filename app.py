import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCrn4KtvCVrbioMd_FbTOvt7gLlTdzVnyQ")

st.title("welcome to gemini chat")


text = st.text_input("enter your question")

model =genai.GenerativeModel('gemini-pro')

chat =model.start_chat(history=[])

if st.button("Click me"):

   response = chat.send_message(text)

   st.write(response.text)
