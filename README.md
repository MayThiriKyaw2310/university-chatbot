Voice based AI virtual Assistant for TU Hmawbi
Description
This project is a voice-based AI virtual assistant designed to respond to voice commands, perform tasks, and answer questions. It utilizes natural language processing (NLP), speech recognition, and machine learning to understand user intent and provide relevant responses.

Features
There will be two features.

Responding the voice command about Technological University TU(Hmawbi) and EC Department
Opening Google Chrome and You Tube by using voice command
API Documentation
Base URL

http://localhost:4444/

Endpoints

POST /postdata
Description: Accepts a voice command (text) and performs the corresponding action (e.g., open apps, perform searches).

Request:

Method: POST
Content-Type: application/json
Body:

{
    "text": "open chrome"
}
Response:

Status: 200 OK
Body:

{
    "audio": "base64_audio_string",
    "speak": "Opening Chrome",
    "listen": "open chrome"
}
POST /stop
Description: Stops the assistant from listening to commands.

Request:

Method: POST
Content-Type: application/json
Body: {}
Response:

Status: 200 OK
Body:

{
    "message": "Stopped"
}
Error Codes

400 Bad Request: Invalid JSON or missing fields.
405 Method Not Allowed: Unsupported HTTP method.
500 Internal Server Error: Server-side failure.
Getting Started
Please start here. Quick Start Guide

Install the required packages by running:

pip install -r requirements.txt
Start the local servers by executing:

python app3.py
Authentication
Currently, no authentication is required to access the API. Users can directly make requests to the endpoints without needing an API key or OAuth token.

Users Guidelines
How to Use the Assistant

The Voice-Based AI Assistant helps you perform tasks by taking simple text commands and answering the knowledge about the TU Hmawbi. Just type or ask what you want to do, and the assistant will respond.

What You Can Say

Open Apps or Websites:
    Example: "open chrome" (opens Chrome)
    Example: "open youtube" (openas YouTube)

Click on Buttons:
    Example: "click on submit button"

Ask Questions:
    Example: "where is Nothern Technological University?"# university-chatbot
