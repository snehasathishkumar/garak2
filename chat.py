import google.generativeai as genai
from dotenv import get_key
import streamlit as st

st.set_page_config(layout='wide')
st.header("Chat with Gemini")

if "messages" not in st.session_state: #initialising chat history
    st.session_state.messages = []

api_key = get_key('.env', key_to_get="GEMINI_API_KEY")

genai.configure(api_key=api_key)

#Defining model
gen_config = genai.GenerationConfig(
    temperature=0.5,
)

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    generation_config=gen_config ) 

# response = model.generate_content("Hi")

user_input = st.chat_input("Enter your query")

if user_input:
    st.session_state["messages"].append({"role":"user", "content":user_input})
    response = model.generate_content(f"{user_input}")
    st.session_state["messages"].append({"role":"assistant", "content":response.text})

for msg in st.session_state["messages"]:
    st.chat_message("role").write(msg["content"])
