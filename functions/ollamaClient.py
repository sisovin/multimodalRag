import requests
import json

class OllamaClient:
    def __init__(self, base_url, model_name, logger):
        self.base_url = base_url
        self.model_name = model_name
        self.logger = logger

    async def get_embeddings_async(self, text):
        request_url = f"{self.base_url}/embeddings"
        payload = {"model": "nomic-embed-text", "prompt": text}

        try:
            response = requests.post(request_url, json=payload)
            response.raise_for_status()
            response_content = response.json()
            return json.dumps(response_content)
        except requests.RequestException as ex:
            self.logger.error(f"Error in get_embeddings_async: {ex}")
            print(f"Error: {ex}")
            return "Error retrieving embeddings."

    async def get_chat_response_async(self, prompt):
        request_url = f"{self.base_url}/generate"
        payload = {"model": self.model_name, "prompt": prompt}

        try:
            response = requests.post(request_url, json=payload)
            response.raise_for_status()
            response_content = response.text  # Get raw text response
            # self.logger.info(f"Raw chat response: {response_content}")
            return response_content
        except requests.RequestException as ex:
            self.logger.error(f"Error in get_chat_response_async: {ex}")
            print(f"Error: {ex}")
            return ""

def format_embeddings_response(embeddings_response):
    try:
        response_json = json.loads(embeddings_response)
        embedding_array = response_json.get("embedding")
        if embedding_array is None:
            return "No embeddings available."
        print("Embeddings array:", ", ".join(map(str, embedding_array)))
        return ", ".join(map(str, embedding_array))
    except Exception as ex:
        print(f"Error formatting embeddings response: {ex}")
        return "Error formatting embeddings."

def format_chat_response(chat_response):
    try:
        if not chat_response.strip():
            return "Empty response received."
        
        string_builder = []
        for line in chat_response.split('\n'):
            if line.strip():
                json_line = json.loads(line)
                message_content = json_line.get("response")
                if message_content:
                    string_builder.append(message_content)
        return "".join(string_builder)
    except json.JSONDecodeError as ex:
        print(f"Error formatting chat response: {ex}")
        return "Error formatting chat response: Invalid JSON."
    except Exception as ex:
        print(f"Error formatting chat response: {ex}")
        return "Error formatting chat response."