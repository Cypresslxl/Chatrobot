import requests

# Replace with your actual xAi API key
XAI_API_KEY = "xai-9ZxSyq868m5SrAagCVEpGqPVZ033tHz9Yr3NtlL2fjvjyyn6z7oxLabt5qPEy64yUzkFFoxeOrnZK6hC"
XAI_API_URL = "https://api.x.ai/v1/chat/completions"

def call_xai_api(messages, model="grok-beta", temperature=0, stream=False):
    """
    Calls the xAi chat completions API.
    
    :param messages: List of messages (e.g., [{"role": "user", "content": "Hello"}])
    :param model: The model to use (default: "grok-beta")
    :param temperature: Controls randomness (default: 0)
    :param stream: Whether to stream the response (default: False)
    :return: JSON response from the API
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {XAI_API_KEY}"
    }
    
    data = {
        "messages": messages,
        "model": model,
        "temperature": temperature,
        "stream": stream
    }
    
    try:
        response = requests.post(XAI_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        # Handle errors (e.g., network issues, invalid API key)
        return {"status": "error", "message": str(e)}