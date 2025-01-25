from flask import Flask, render_template, request, jsonify  # Added jsonify import

from transformers import pipeline

# xAi
from controller import call_xai_api


app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Flask route to handle chat requests.
    """
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract messages from the request
    messages = data.get("messages", [])
    
    if not messages:
        return jsonify({"status": "error", "message": "Messages are required"}), 400
    
    # Call the xAi API
    result = call_xai_api(messages)
    
    # Return the API response
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# Load the pre-trained model
model = pipeline("text-generation", model="gpt2")

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/test",methods=["GET"])
def test():
    return "this is a message from chatbot !!!"

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.form["user_input"]
#     response = model(user_input, max_length=50, num_return_sequences=1)[0]["generated_text"]
#     return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')