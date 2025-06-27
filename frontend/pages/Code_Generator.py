import streamlit as st
import requests

st.title("Code Generator")
prompt = st.text_area("Enter prompt for code generation:", "")
if st.button("Generate Code"):
    resp = requests.post("http://127.0.0.1:8000/ai/generate-code", json={"prompt": prompt})
    if resp.ok:
        st.code(resp.json()["response"])
    else:
        st.error(resp.text)
