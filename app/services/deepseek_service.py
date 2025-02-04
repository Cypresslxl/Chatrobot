from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

def get_deepseek_response(user_message):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_message},
        ],
        stream=False
    )
    return response.choices[0].message.content

def process_txt_file(file_content):
    # Use the file content as the user message
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": f"Please analyze the following text and provide a response:\n{file_content}"},
        ],
        stream=False
    )
    return response.choices[0].message.content