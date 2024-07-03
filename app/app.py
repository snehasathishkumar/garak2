import streamlit as st
import json
from app.cli import run_garak_command
import subprocess
import streamlit.components.v1 as components

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

if "probes" not in st.session_state:
     st.session_state["probes"] = None
    
if "generations" not in st.session_state:
    st.session_state["generations"] = None


#input 
# if not st.session_state["model_type"]:
#     st.session_state["model_type"] = st.selectbox(label= "Select your model Name",options=model_names )

# if not st.session_state["model_name"]:
#     st.session_state['model_name'] = st.text_input(label = "Enter Model Type ",type="default")

# if not st.session_state["probes"]:
#     st.session_state["probes"] = st.selectbox(label= " Select the probe ",options = probes )

# if not st.session_state["generations"]:
#     st.session_state["generations"] = st.text_input(label = " Enter Number of Generations ", type = "default")

# if st.button("Start test"):
#     print(model_type,generations,model_name,probes)

with st.form(key='my_form'):
    model_type = st.selectbox(label= "Select your Model Type",options=model_names , placeholder= " Choose an option" )
    model_name = st.text_input(label = "Enter Model Name ", type = "default" )
    probes = st.selectbox(label= " Select the probe ",options = probes , placeholder =  " Choose an option")
    generations = st.text_input(label = " Enter Number of Generations ", type = "default")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        run_garak_command(model_type,model_name,probes,generations)
        # print(model_type,model_name,probes,generations)
    # submit_button = st.form_submit_button(label='Submit')
        # # name ="report1"
        # st.write("test html import")

        # HtmlFile = open("report1.report.html", 'r', encoding='utf-8')
        # source_code = HtmlFile.read() 
        # print(source_code)
        # components.html(source_code,height=2000)

    
# print(st.session_state['model_name'] )
# m.run_garak_command(model_type,model_name,generations)