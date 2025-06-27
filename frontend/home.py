import streamlit as st
import requests

# ---------------------------------------------------
# ⚡️ CONFIGURE PAGE
# ---------------------------------------------------
st.set_page_config(page_title="SmartSDLC Dashboard", layout="wide")

# ---------------------------------------------------
# 🎨 LOTTIE ANIMATION UTILITY
# ---------------------------------------------------
def load_lottie_url(url: str):
    """Load Lottie animation from a URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# ---------------------------------------------------
# ⚡️ MAIN PAGE
# ---------------------------------------------------
st.markdown("""
# 👋 Welcome to SmartSDLC
### AI-Enhanced Software Development Lifecycle
Revolutionize your SDLC with AI:
- 📄 **Upload Requirements** and classify
- 💻 **Generate Production-Ready Code**
- 🐞 **Fix Bugs**
- ✅ **Write Test Cases**
- 📋 **Summarize Source Code**
- 💬 **Get Instant Chat Support**
""")

# ---------------------------------------------------
# 🎥 LOTTIE ANIMATION
# ---------------------------------------------------
lottie_url = "https://assets9.lottiefiles.com/packages/lf20_yr1zz3wv.json"  # Example animation
animation = load_lottie_url(lottie_url)

if animation:
    st.lottie(animation, height=300)

# ---------------------------------------------------
# 🔥 PAGE NAVIGATION CARDS
# ---------------------------------------------------
st.markdown("## 🚀 Get Started:")

columns = st.columns(3)

with columns[0]:
    st.markdown("""
    ### 📄 Upload & Classify
    Quickly process PDFs and categorize requirements.
    [Go to Page ➔](Upload_and_Classify)
    """)

    st.markdown("""
    ### 💻 Code Generator
    AI-crafted code snippets from prompts.
    [Go to Page ➔](Code_Generator)
    """)

with columns[1]:
    st.markdown("""
    ### ✅ Test Generator
    Automatically write test cases for your code.
    [Go to Page ➔](Test_Generator)
    """)

    st.markdown("""
    ### 🐞 Bug Fixer
    Fix syntax and logical errors in seconds.
    [Go to Page ➔](Bug_Fixer)
    """)

with columns[2]:
    st.markdown("""
    ### 📋 Code Summarizer
    Get plain-English summaries of complex code.
    [Go to Page ➔](Code_Summarizer)
    """)

    st.markdown("""
    ### 💬 Feedback
    Collect user feedback and enhance your project.
    [Go to Page ➔](Feedback)
    """)

# ---------------------------------------------------
# 💬 SIMPLE CHAT
# ---------------------------------------------------
from simple_chat import chat_widget
chat_widget()

# ---------------------------------------------------
# ✅ END
# ---------------------------------------------------
