import streamlit as st
import json
import main as m

st.title("garak")

with open("model_names.json", "r") as read_content: 
    model_names=json.load(read_content)['model_names']

model_type = st.selectbox(label= " Select your model type" , options = model_names )
model_name = st.text_input(label = " Enter Model Name ")
generations = st.text_input(label = " Enter Number of Generations ")

m.run_garak_command("huggingface")