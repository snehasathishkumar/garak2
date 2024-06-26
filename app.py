import streamlit as st
import json
import main as m

st.set_page_config(layout='wide')

st.title("garak")

with open("model_names.json", "r") as read_content: 
    model_names=json.load(read_content)['model_names']

with open("probes.json", "r") as read_content: 
    probes=json.load(read_content)['probes']

#initialization
if "model_type" not in st.session_state:
    st.session_state["model_type"] = None

if "model_name" not in st.session_state:
    st.session_state["model_name"] = None

if "generations" not in st.session_state:
    st.session_state["generations"] = None

# if "submit" not in st.session_state:
#      st.session_state["submit"] = None

# if "probes" not in st.session_state:
#      st.session_state["probes"] = None

#input 
if not st.session_state["model_type"]:
        model_type = st.selectbox(label= " Select your model Name",options=model_names )

if not st.session_state["model_name"]:
    model_name = st.text_input(label = " Enter Model Type ",key="model_name")

if not st.session_state["model_type"]:
        model_type = st.selectbox(label= " Select the probe ",options = probes )

if not st.session_state["generations"]:
    generations = st.text_input(label = " Enter Number of Generations ")

if st.button("Start test"):
    print(model_type,generations,model_name,probes)

# m.run_garak_command(model_type,model_name,generations)