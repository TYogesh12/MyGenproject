import streamlit as st
import requests

st.title("Bug Fixer")
st.markdown("Paste your buggy code, and we'll fix it for you.")

code_snippet = st.text_area("Enter your buggy code:", "")
if st.button("Fix Bug"):
    if code_snippet.strip():
        response = requests.post("http://127.0.0.1:8000/ai/fix-bug", json={"prompt": code_snippet})
        if response.ok:
            st.markdown("### Fixed Code")
            st.code(response.json()["response"])
        else:
            st.error("Error from backend.")
    else:
        st.warning("Please paste some code.")
