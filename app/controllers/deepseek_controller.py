from flask import Blueprint, request, jsonify
from app.services.deepseek_service import get_deepseek_response, process_txt_file
import logging

# Create a Blueprint for DeepSeek routes
deepseek_bp = Blueprint('deepseek', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@deepseek_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    logger.info(f"Received message: {user_message}")

    if not user_message:
        logger.error("No message provided")
        return jsonify({"error": "No message provided"}), 400

    try:
        assistant_response = get_deepseek_response(user_message)
        logger.info(f"Assistant response: {assistant_response}")
        return jsonify({"response": assistant_response})

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@deepseek_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.error("No file uploaded")
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # Check if the file has a .txt suffix
    if not file.filename.endswith('.txt'):
        logger.error("Invalid file type. Only .txt files are allowed")
        return jsonify({"error": "Invalid file type. Only .txt files are allowed"}), 400

    try:
        # Process the file and get the response
        file_content = file.read().decode('utf-8')
        assistant_response = process_txt_file(file_content)
        logger.info(f"Assistant response: {assistant_response}")
        return jsonify({"response": assistant_response})

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500