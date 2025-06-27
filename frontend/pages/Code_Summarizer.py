import streamlit as st
import requests

st.title("Code Summarizer")
st.markdown("Enter your code, and we'll summarize it.")

user_code = st.text_area("Enter code:", "")
if st.button("Summarize"):
    if user_code.strip():
        response = requests.post("http://127.0.0.1:8000/ai/summarize-code", json={"prompt": user_code})
        if response.ok:
            st.markdown("### Summary")
            st.write(response.json()["response"])
        else:
            st.error("Error from backend.")
    else:
        st.warning("Please paste some code.")
