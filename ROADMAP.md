# ROADMAP

# multimodalRag

## Brainstorming Ideas
multimodalRag is a Python application that integrates with the streamlit and Ollama AI API. It provides functionalities to retrieve text embeddings and interact with a chatbot, logging interactions and saving chat history as customized save settings of the selected modal as you want to use a modal with chatbot for chatting purpose and save chat history with chat_history.json file in the logregistry folder and load the save chat history to continue the user session chat.

## Features
- Retrieve text embeddings using the Ollama AI API.
- Chat with the Ollama AI chatbot.
- Log interactions and save chat history.
- Continuous chat loop until the user exits.
- Create logregistry directory
- Store chat_history.json 
- Save logger name ollamalog.log
- settings.py (using selecbox to save the selected model that download them into the Ollama model library)
- 1. Logger.py under the functions directory (functions.logger impport Logger)
- 2. OllamaClient.py under the functions directory
- 3. main.py under the root directory of the project(using streamlit User Interface with chat_input of streamlit library)

## Prerequisites
- Ollama model Server
- apiBase = "http://localhost:11434/api"; 
- modelName = "llama3.2:3b";
- Ollama embeddings: "model": "nomic-embed-text"

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/sisovin/multimodalRag.git
cd D:\learnPython\multimodalRag\
D:\learnPython\multimodalRag>llama\Scripts\activate
(llama) D:\learnPython\multimodalRag>
