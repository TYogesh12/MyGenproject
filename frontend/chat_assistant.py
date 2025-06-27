import streamlit as st
import requests

def show_chat_assistant():
    # Initialize session state
    if 'chat_open' not in st.session_state:
        st.session_state.chat_open = False
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # CSS for floating chat
    st.markdown("""
    <style>
    .chat-button {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: #007bff;
        color: white;
        border: none;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 1000;
    }
    
    .chat-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0,0,0,0.5);
        z-index: 1001;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .chat-window {
        width: 400px;
        height: 600px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }
    
    .chat-header {
        background: #007bff;
        color: white;
        padding: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: bold;
    }
    
    .chat-messages {
        flex: 1;
        padding: 20px;
        overflow-y: auto;
        background: #f8f9fa;
    }
    
    .message {
        margin: 10px 0;
        padding: 12px 16px;
        border-radius: 15px;
        max-width: 80%;
        word-wrap: break-word;
    }
    
    .user-message {
        background: #007bff;
        color: white;
        margin-left: auto;
        border-radius: 15px 15px 5px 15px;
    }
    
    .bot-message {
        background: white;
        color: #333;
        border: 1px solid #ddd;
        border-radius: 15px 15px 15px 5px;
    }
    
    .welcome-message {
        background: #e3f2fd;
        color: #1976d2;
        border: 1px solid #bbdefb;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    .chat-input {
        padding: 20px;
        border-top: 1px solid #ddd;
        background: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Show chat button when closed
    if not st.session_state.chat_open:
        if st.button("💬", key="open_chat"):
            st.session_state.chat_open = True
            st.rerun()
        
        # Position the button
        st.markdown("""
        <script>
        const buttons = document.querySelectorAll('button');
        buttons.forEach(btn => {
            if (btn.textContent.includes('💬')) {
                btn.style.position = 'fixed';
                btn.style.bottom = '30px';
                btn.style.right = '30px';
                btn.style.width = '60px';
                btn.style.height = '60px';
                btn.style.borderRadius = '50%';
                btn.style.background = '#007bff';
                btn.style.color = 'white';
                btn.style.border = 'none';
                btn.style.fontSize = '24px';
                btn.style.zIndex = '1000';
                btn.style.boxShadow = '0 4px 12px rgba(0,0,0,0.3)';
            }
        });
        </script>
        """, unsafe_allow_html=True)

    # Show chat window when open
    if st.session_state.chat_open:
        st.markdown("""
        <div class="chat-overlay">
            <div class="chat-window">
                <div class="chat-header">
                    <span>🤖 SmartSDLC Assistant</span>
                </div>
                <div class="chat-messages">
                    <div class="message welcome-message">
                        👋 Hello! I'm your SmartSDLC Assistant. How can I help you today?
                    </div>
        """, unsafe_allow_html=True)
        
        # Display messages
        for msg_type, content in st.session_state.messages:
            css_class = "user-message" if msg_type == "user" else "bot-message"
            st.markdown(f'<div class="message {css_class}">{content}</div>', unsafe_allow_html=True)
        
        st.markdown('</div><div class="chat-input">', unsafe_allow_html=True)
        
        # Input area
        col1, col2, col3 = st.columns([5, 1, 1])
        
        with col1:
            user_input = st.text_input("Message", key="msg_input")
        
        with col2:
            send_clicked = st.button("Send", key="send")
        
        with col3:
            close_clicked = st.button("✕", key="close")
        
        st.markdown('</div></div></div>', unsafe_allow_html=True)
        
        # Handle send
        if send_clicked and user_input.strip():
            st.session_state.messages.append(("user", user_input))
            
            try:
                response = requests.post("http://127.0.0.1:8000/ai/chat", 
                                       json={"prompt": user_input}, timeout=30)
                if response.ok:
                    bot_reply = response.json().get("response", "Sorry, no response.")
                else:
                    bot_reply = "Sorry, I'm having trouble right now."
                    
                st.session_state.messages.append(("bot", bot_reply))
            except:
                st.session_state.messages.append(("bot", "Sorry, something went wrong."))
            
            st.rerun()
        
        # Handle close
        if close_clicked:
            st.session_state.chat_open = False
            st.session_state.messages = []
            st.rerun()