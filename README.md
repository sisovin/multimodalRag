# multimodalRag Project

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Set up the virtual environment](#step-2-set-up-the-virtual-environment)
  - [Step 3: Install dependencies](#step-3-install-dependencies)
  - [Step 4: Run the application](#step-4-run-the-application)
- [Code Snippet Example](#code-snippet-example)
  - [Main](#main-mainpy)
  - [Logger](#logger-loggerpy)
  - [OllamaClient](#ollamaclient-ollamaclientpy)
  - [Settings](#settings-settingspy)
  - [Requirements](#requirements-requirementstxt)

## Description
multimodalRag is a Python application that integrates with Streamlit and the Ollama AI API. It provides functionalities to retrieve text embeddings and interact with a chatbot, logging interactions and saving chat history.

## Features
- Retrieve text embeddings using the Ollama AI API.
- Chat with the Ollama AI chatbot.
- Log interactions and save chat history.
- Continuous chat loop until the user exits.
- Create logregistry  directory.
- Store chat_history.json.
- Save logger name `ollamalog.log`.
- Settings to select and save the model.

## Prerequisites
- Ollama model Server
- API Base: `http://localhost:11434/api`
- Model Name: `llama3.2:3b`
- Ollama embeddings: `"model": "nomic-embed-text"`

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/sisovin/multimodalRag.git
cd multimodalRag
```

### Step 2: Set up the virtual environment
```bash
python -m venv llama
source llama/bin/activate  # On Windows use 

activate


```

### Step 3: Install dependencies
```bash
pip install -r 

requirements.txt


```

### Step 4: Run the application
```bash
python 

main.py


```

## Code Snippet Example

### Main [main.py]

### Logger [logger.py]

### OllamaClient [ollamaClient.py]

### Settings [settings.py]

### Requirements [requirements.txt]

streamlit
streamlit-chat
requests
asyncio
