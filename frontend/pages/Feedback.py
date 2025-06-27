import streamlit as st
import requests

st.title("Feedback")
st.markdown("Provide feedback about SmartSDLC.")

name = st.text_input("Your Name:", "")
email = st.text_input("Your Email:", "")
feedback = st.text_area("Feedback:", "")

if st.button("Submit Feedback"):
    if name and email and feedback:
        payload = {"name": name, "email": email, "feedback": feedback}
        response = requests.post("http://127.0.0.1:8000/feedback", json=payload)
        if response.ok:
            st.success("Thank you for your feedback! 🙌")
        else:
            st.error("Error submitting feedback.")
    else:
        st.warning("Please fill out all fields.")
