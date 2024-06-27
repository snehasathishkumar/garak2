import streamlit as st
import streamlit.components.v1 as components


st.header("test html import")

HtmlFile = open("report1.report.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code,height=2000)

if st.button('Display HTML Document'):
    st.markdown('<iframe src="report1.report.html" width="700" height="400"></iframe>', unsafe_allow_html=True)