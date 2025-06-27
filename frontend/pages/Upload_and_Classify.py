import streamlit as st
import requests

st.title("Upload & Classify Requirements")
st.markdown("Upload a requirement (or paste text) to classify into SDLC phases.")

user_input = st.text_area("Enter requirement text:", "")
if st.button("Classify"):
    if user_input.strip():
        response = requests.post("http://127.0.0.1:8000/ai/classify-requirement", json={"prompt": user_input})
        if response.ok:
            st.markdown("### Result")
            st.write(response.json()["response"])
        else:
            st.error("Error from backend.")
    else:
        st.warning("Please enter some text.")
