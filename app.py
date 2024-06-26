import streamlit as st
import json
import main as m

st.title("garak")

with open("model_names.json", "r") as read_content: 
    model_names=json.load(read_content)['model_names']

#initialization
if "model_type" not in st.session_state:
    st.session_state["model_type"] = None

if "model_name" not in st.session_state:
    st.session_state["model_name"] = None

if "generations" not in st.session_state:
    st.session_state["generations"] = None

if "submit" not in st.session_state:
     st.session_state["submit"] = None

# if "probes" not in st.session_state:
#      st.session_state["probes"] = None

#input 
if not st.session_state["model_type"]:
        model_type = st.selectbox(label= " Select your model Name",options=model_names )

if not st.session_state["model_name"]:
    model_name = st.text_input(label = " Enter Model Type ",key="model_name")

# if not st.session_state["probes "]:
#     st.session_state["probes "] =st.text_input("Enter Webpage URL", type="default")

if not st.session_state["generations"]:
    generations = st.text_input(label = " Enter Number of Generations ")

submit = False
submit = st.button("Click to run test")

if st.session_state[submit]:
     print("works")

# m.run_garak_command(model_type,model_name,generations)