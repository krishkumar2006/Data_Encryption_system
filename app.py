import streamlit as st
from cryptography.fernet import Fernet

# ---------------------------
# Page Setup & Styling
st.set_page_config(page_title="Secure Data encrytion", layout="centered")
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0d0d0d, blue);
    color: #ffe6f7;
}
h1, h2 {
    text-align: center;
    color: #ffd700;
    text-shadow: 1px 1px #000;
}
.stTextInput, .stTextArea, .stButton>button {
    font-size: 18px;
}
.stButton>button {
    background-color: #ff1493;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1rem;
}
.stButton>button:hover {
    background-color: #e60073;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: #999;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Fernet Setup
if "cipher" not in st.session_state:
    key = Fernet.generate_key()
    st.session_state.cipher = Fernet(key)

# ---------------------------
# Encryption Page (Only Page)
st.title("🔒 Secure Data Encryption")
st.subheader("Use this tool to **encrypt or decrypt** your messages securely.")

message = st.text_area("Enter your message to encrypt/decrypt:", height=200)

col1, col2 = st.columns(2)

if col1.button("Encrypt"):
    if message:
        encrypted = st.session_state.cipher.encrypt(message.encode()).decode()
        st.success("Encrypted Message:")
        st.code(encrypted)
    else:
        st.warning("Please enter a message to encrypt.")

if col2.button("Decrypt"):
    try:
        if message:
            decrypted = st.session_state.cipher.decrypt(message.encode()).decode()
            st.success("Decrypted Message:")
            st.code(decrypted)
        else:
            st.warning("Please enter an encrypted message.")
    except:
        st.error("Invalid encrypted text.")