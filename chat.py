import streamlit as st
from dotenv import get_key
from langchain_google_genai import GoogleGenerativeAI as genai
from langchain_experimental.agents import create_csv_agent
import pandas as pd


api_key = get_key(".env", key_to_get="GEMINI_API_KEY")
llm = genai(model="gemini-1.5-flash-latest",google_api_key=api_key)

st.set_page_config(page_title="Ask your CSV")
st.header("Ask your CSV 📈")

if "messages" not in st.session_state: #initialising chat history
    st.session_state.messages = []

#defining agent
agent = create_csv_agent(llm=llm, path="train.csv",pandas_kwargs={"nrows" : 10},allow_dangerous_code=True, verbose = True)

csv_file = st.file_uploader("Upload a CSV file", type="csv")

if csv_file is not None:
    user_input = st.chat_input("Enter your query")
    if user_input:
        st.session_state["messages"].append({"role":"user", "content":user_input})

        response = 

        st.session_state["messages"].append({"role":"assistant", "content":response})

    for msg in st.session_state["messages"]:
        st.chat_message("role").write(msg["content"])
