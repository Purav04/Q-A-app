# Q&A Chatbot
# from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
import os
load_dotenv()

import streamlit as st

# fuction to load OpenAI and get response
def get_openai_response(question):
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response

# initializing streamlit
st.set_page_config(page_title="Q & A Demo")

st.header("langchain Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if ask button clicked
if submit:
    response = get_openai_response(input)
    st.subheader("The Response is")
    st.write(response)