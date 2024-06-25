import streamlit as st
import json
import main as m

st.title("garak")

with open("model_names.json", "r") as read_content: 
    model_names=json.load(read_content)['model_names']

if "model_type" not in st.session_state:
    st.session_state["model_type"] = None

if "model_name" not in st.session_state:
    st.session_state["model_name"] = None

if "generations" not in st.session_state:
    st.session_state["generations"] = None

if not st.session_state["uploaded_file_sum"]:
        st.session_state["uploaded_file_sum"] = st.file_uploader("Upload your file here")

model_type = st.selectbox(label= " Select your model Name" , options = model_names )
model_name = st.text_input(label = " Enter Model Type ")
generations = st.text_input(label = " Enter Number of Generations ")

if model_type!
m.run_garak_command(model_type,model_name,generations)