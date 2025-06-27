import streamlit as st
import requests

st.title("Test Generator")
st.markdown("Enter code or requirement to generate test cases.")

user_input = st.text_area("Enter requirement or code:", "")
if st.button("Generate Test Cases"):
    if user_input.strip():
        response = requests.post("http://127.0.0.1:8000/ai/generate-test", json={"prompt": user_input})
        if response.ok:
            st.markdown("### Generated Tests")
            st.code(response.json()["response"])
        else:
            st.error("Error from backend.")
    else:
        st.warning("Please enter some input.")
