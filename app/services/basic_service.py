from openai import OpenAI
from config import Config

# Initialize the OpenAI client
client = OpenAI(api_key=Config.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

def get_deepseek_response(user_message, model="deepseek-chat", stream=False, conversation_history=None):
    """
    Get a response from the DeepSeek model.

    Args:
        user_message (str): The message from the user.
        model (str): The model to use for the response. Default is "deepseek-chat".
        stream (bool): Whether to stream the response. Default is False.
        conversation_history (list): A list of previous messages in the conversation. Default is None.

    Returns:
        str or generator: The response from the model. If streaming, returns a generator.
    """
    if conversation_history is None:
        conversation_history = []

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=conversation_history,
            stream=stream
        )

        if stream:
            # If streaming, return a generator that yields chunks of the response
            def response_generator():
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            return response_generator()
        else:
            # If not streaming, return the full response
            assistant_message = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": assistant_message})
            return assistant_message

    except Exception as e:
        # Handle any errors that occur during the API call
        print(f"An error occurred: {e}")
        return None

def chat_with_deepseek():
    """
    Start an interactive chat session with the DeepSeek model.
    """
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Welcome to the DeepSeek chat! Type 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_deepseek_response(user_message, conversation_history=conversation_history)
        if response:
            print(f"DeepSeek: {response}")

if __name__ == "__main__":
    # Example usage
    chat_with_deepseek()