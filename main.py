import streamlit as st
import ollama

def chat_with_mistral(prompt):
    response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Streamlit UI
st.title("Ollama + Mistral Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response from Mistral
    response = chat_with_mistral(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with st.chat_message("assistant"):
        st.write(response)
