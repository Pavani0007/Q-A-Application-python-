from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
        # print("response: ",response)
        parts=response.candidates[0].content.parts
        text =' '.join(part.text for part in parts)
        return text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Invoice Extractor ")
input=st.text_input("input the prompt",key="input")
uploaded_file=st.file_uploader("choose the image...",type=["jpg","jpeg","png"])
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Invoice Image.")

submit=st.button("Tell me about the image")



if submit:
    response=get_gemini_response(input,image)
    st.subheader("the response is:")
    st.write(response)


