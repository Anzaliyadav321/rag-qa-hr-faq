import os
# os.environ["STREAMLIT_WATCHER_TYPE"] = "none" 

import streamlit as st
from app.qa_pipeline import run_qa_pipeline

st.set_page_config(page_title="HR FAQ Assistant", layout="centered")

st.title("HR FAQ Assistant")
st.write("Ask me any HR-related question!")

user_question = st.text_input("Your Question")

if user_question:
    with st.spinner("Thinking..."):
        response = run_qa_pipeline(user_question)
    st.markdown("### Answer:")    
    st.success(response)




