import streamlit as st
import requests
import os
import json
from functions.logger import Logger

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
    
def load_settings():
    model_path = r"D:\Ollama\Models\manifests\registry.ollama.ai\library"
    models = []
    if os.path.exists(model_path):
        for model in os.listdir(model_path):
            model_dir = os.path.join(model_path, model)
            if os.path.isdir(model_dir):
                for version in os.listdir(model_dir):
                    version_path = os.path.join(model_dir, version)
                    if os.path.isfile(version_path):
                        model_version = f"{model}:{version}"
                        models.append(model_version)
        logger.info(f"Models found: {models}")
    else:
        logger.error(f"Model path does not exist: {model_path}")

    settings_file = 'settings.json'
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            settings = json.load(f)
            return settings.get('model_options', models), settings.get('selected_model', None)
    return models, None

def download_model(model_name):
    api_base = "http://localhost:11434/api"
    request_url = f"{api_base}/download_model"
    payload = {"model_name": model_name}

    try:
        response = requests.post(request_url, json=payload)
        response.raise_for_status()
        st.success(f"Model {model_name} downloaded successfully!")
    except requests.RequestException as ex:
        st.error(f"Error downloading model: {ex}")

def main():
    st.title("Ollama Model Library")
    model_options = load_settings()
    selected_model = st.selectbox("Select a model to download", model_options)

    if st.button("Download Model"):
        download_model(selected_model)

if __name__ == "__main__":
    main()