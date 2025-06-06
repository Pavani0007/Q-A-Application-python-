from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response=model.generate_content(question)
    print("response: ",response)
    parts=response.candidates[0].content.parts
    text =' '.join(part.text for part in parts)
    return text

st.set_page_config(page_title="q&A demo")
st.header("gemini q&a Application")
input=st.text_input("ask your question:",key="input")
submit=st.button("submit")


if submit:
    response=get_gemini_response(input)
    st.subheader("the response is:")
    st.write(response)


