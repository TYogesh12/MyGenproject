import streamlit as st
import requests

def chat_widget():
    if 'chat_open' not in st.session_state:
        st.session_state.chat_open = False
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []

    # Chat button
    if not st.session_state.chat_open:
        if st.button("💬 Chat", key="open_chat_btn"):
            st.session_state.chat_open = True
            st.rerun()

    # Chat window
    if st.session_state.chat_open:
        st.markdown("### 🤖 SmartSDLC Assistant")
        
        # Messages
        for role, msg in st.session_state.chat_messages:
            if role == "user":
                st.write(f"**You:** {msg}")
            else:
                st.write(f"**Assistant:** {msg}")
        
        # Input
        col1, col2, col3 = st.columns([6, 1, 1])
        
        with col1:
            user_msg = st.text_input("Type message", key="chat_msg")
        with col2:
            if st.button("Send", key="send_msg"):
                if user_msg.strip():
                    st.session_state.chat_messages.append(("user", user_msg))
                    
                    try:
                        response = requests.post("http://127.0.0.1:8000/ai/chat", 
                                               json={"prompt": user_msg}, timeout=30)
                        if response.ok:
                            reply = response.json().get("response", "No response")
                        else:
                            reply = "Error connecting"
                        st.session_state.chat_messages.append(("bot", reply))
                    except:
                        st.session_state.chat_messages.append(("bot", "Error occurred"))
                    
                    st.rerun()
        
        with col3:
            if st.button("Close", key="close_chat"):
                st.session_state.chat_open = False
                st.session_state.chat_messages = []
                st.rerun()