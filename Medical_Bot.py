from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model= genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    prompt = (
        "You are a helpful medical assistant. Only answer medical-related questions. "
        "If the question is not about medicine, health, symptoms, diseases, treatment, or the human body, "
        "respond with: 'I'm only able to answer medical-related questions.'\n\n"
        f"Question: {question}"
    )
    response=model.generate_content(prompt)
    # print("response: ",response)
    parts=response.candidates[0].content.parts
    text =' '.join(part.text for part in parts)
    return text

st.set_page_config(page_title="Medical Q&A Demo")
st.header("Gemini Medical Q&A Application")
input=st.text_input("ask your Medical question:",key="input")
submit=st.button("submit")


if submit:
    response=get_gemini_response(input)
    st.subheader("the response is:")
    st.write(response)


