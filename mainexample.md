```python
import json
import os
import asyncio
import streamlit as st
from streamlit_chat import message
from functions.logger import Logger
from functions.ollamaClient import OllamaClient, format_embeddings_response, format_chat_response
from settings import load_settings

# Ensure the logs directory exists
log_dir = 'logregistry'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
      
# Initialize logger
try:
    logger = Logger(log_file=os.path.join('logregistry', 'ollamalog.log'), level=Logger.LEVEL_INFO)
except PermissionError as e:
    st.error(f"Permission error: {e}")
    logger = None

# Function to save chat history
def save_chat_history(chat_history, dir, file_name):
    if logger:
        logger.info("Saving chat history...")
    file_path = os.path.join(dir, file_name)
    with open(file_path, 'w') as f:
        json.dump(chat_history, f)
    if logger:
        logger.info("Chat history saved successfully")

# Function to load chat history
def load_chat_history(dir, file_name):
    if logger:
        logger.info("Loading chat history...")
    file_path = os.path.join(dir, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                if logger:
                    logger.info("Chat history loaded successfully")
                return json.load(f)
        except json.JSONDecodeError:
            if logger:
                logger.error("Error decoding JSON from chat history file")
            return []
    if logger:
        logger.info("No chat history found")
    return []

async def main():
    api_base = "http://localhost:11434/api"
    # Load settings
    model_options, selected_model = load_settings()
    if not selected_model:
        selected_model = "llama3.2:3b"  # Default model if none is selected
    client = OllamaClient(api_base, selected_model, logger)

    st.title("User with Chatbot Talk: 🤖")
    st.write("Enter your text to get embeddings and interact with the chatbot.")
    # Load chat history if available
    chat_history_file = 'chat_history.json'
    st.session_state.messages = load_chat_history('logregistry', chat_history_file) if chat_history_file else []

    text = st.text_input("Enter your text to get embeddings")
    if st.button("Get Embeddings"):
        if not text:
            st.error("Text cannot be null or empty.")
            if logger:
                logger.error("User entered an empty text for embeddings.")
        elif text.lower() == "exit":
            st.stop()
        else:
            embeddings_response = await client.get_embeddings_async(text)
            readable_embeddings = format_embeddings_response(embeddings_response)
            if logger:
                logger.info(f"Retrieved embeddings for text: {text}")
            st.write(f"Retrieved embeddings for text: {text}")

    # Sidebar for Settings Model Choice     
    with st.sidebar:
        st.title("Settings")
        st.write("Choose a model to interact with the chatbot.")
        selected_model = st.selectbox("Select a model to interact with the chatbot", model_options, index=model_options.index(selected_model) if selected_model in model_options else 0)
        if st.sidebar.button("Save Settings"):
            settings = {
                'model_options': model_options,
                'selected_model': selected_model
            }
            with open('settings.json', 'w') as f:
                json.dump(settings, f)
            st.write(f"Selected model: {selected_model}")       
            st.sidebar.success("Settings saved successfully.")
    
    # Set Chat Interface
    for i, msg in enumerate(st.session_state.messages):
        message(msg["Content"], is_user=msg["role"] == "user", key=str(i))
    
    # Chat Interface
    if user_prompt := st.chat_input("Enter your prompt for the chat"):
        st.session_state.messages.append({"role": "user", "Content": user_prompt})
        message(user_prompt, is_user=True)
        if logger:
            logger.info(f"User: {user_prompt}")
        if user_prompt:
            if user_prompt.lower() == "exit":
                st.stop()
            else:
                chat_response = await client.get_chat_response_async(user_prompt)
                readable_chat_response = format_chat_response(chat_response)
                st.session_state.messages.append({"role": "bot", "Content": readable_chat_response})
                message(readable_chat_response, is_user=False)
                if logger:
                    logger.info(f"Received chat response for prompt: {user_prompt}")

                chat_history = st.session_state.messages
                save_chat_history(chat_history, 'logregistry', chat_history_file)

if __name__ == "__main__":
    asyncio.run(main())

```