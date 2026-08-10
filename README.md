# WhatsApp AI Customer Support App

A full-stack WhatsApp-style customer support application built with React, FastAPI, SQLite, LangGraph, and Groq LLaMA. The application receives customer messages through a FastAPI webhook, analyzes the message intent, generates an AI-powered response, and stores the conversation in SQLite.

## Features

- Receives incoming messages through a FastAPI webhook
- Detects message intent:
  - Greeting
  - Pricing
  - Support
  - General
- Generates AI replies using Groq LLaMA through LangGraph
- Maintains conversation history per user
- Stores incoming and outgoing messages in SQLite
- Provides APIs to send and retrieve messages
- Supports message status updates such as sent, delivered, and read
- Handles text, location, and contact messages through the webhook
- Pydantic validation for API request data
- Error handling for API and database operations
- React-based chat dashboard for viewing conversations

## Tech Stack

| Layer           | Technology                        |
|-----------------|-----------------------------------|
| Backend         | Python, FastAPI, SQLAlchemy       |
| Database        | SQLite                            |
| AI Workflow     | LangGraph, LangChain              |
| LLM             | Groq LLaMA 3.1                    |
| Frontend        | React, Vite, Axios                |
| API Testing     | Swagger        |
| Version Control | Git, GitHub                       |

## Project Structure

```
whatsapp-ai-app/
├── app/
│   ├── ai/
│   │   ├── graph.py          # LangGraph workflow
│   │   ├── nodes.py          # Intent, LLM and response formatting nodes
│   │   ├── state.py          # AIState definition
│   │   └── tools.py          # AI helper tools
│   │
│   └── main.py               # FastAPI application entry point
│
├── config/
│   └── settings.py           # Application configuration
│
├── database/
│   ├── database.py           # SQLite database connection
│   └── models.py             # SQLAlchemy models
│
├── routes/
│   ├── webhook.py            # POST /webhook
│   └── messages.py           # Message APIs
│
├── services/
│   └── whatsapp.py           # WhatsApp message service
│
├── schemas/
│   └── message.py            # Pydantic request/response schemas
│
├── frontend/
│   └──                       # React + Vite frontend
│
├── requirements.txt
├── .env
└── README.md
```

## Setup

### Backend

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=<your_groq_api_key
DATABASE_URL=sqlite:///./whatsapp.db
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

### Frontend

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

The React application will be available through the Vite development server.

## API Endpoints

| Method | Endpoint                        | Description                                                  |
|--------|---------------------------------|--------------------------------------------------------------|
| POST   | `/webhook`                      | Receives an incoming message and processes it through LangGraph |
| GET    | `/messages`                     | Retrieves all stored messages                                |
| GET    | `/messages/{phone}`             | Retrieves messages for a specific phone number               |
| POST   | `/send-message`                 | Sends and stores an outgoing message                         |
| PATCH  | `/messages/{message_id}/status` | Updates the message delivery status                          |

## AI Workflow

The AI chatbot uses a LangGraph workflow to process every incoming message.

```
Customer Message
        ↓
FastAPI /webhook
        ↓
Store Message in SQLite
        ↓
Retrieve Conversation History
        ↓
LangGraph Workflow
        ↓
understand_message
        ↓
Intent Classification
        ↓
generate_reply
        ↓
Groq LLaMA
        ↓
format_response
        ↓
AI Response
        ↓
Store Response in SQLite
        ↓
Return Response
```

## LangGraph Nodes

### 1. `understand_message`

Analyzes the incoming customer message and identifies the intent as:

- `greeting`
- `pricing`
- `support`
- `general`

### 2. `generate_reply`

Uses the detected intent, customer message, and conversation context to generate a response using the Groq LLaMA model.

### 3. `format_response`

Formats the generated AI response before returning it to the webhook.

## Message Flow

```
Customer
   ↓
FastAPI Webhook
   ↓
Pydantic Validation
   ↓
SQLite
   ↓
Conversation History
   ↓
LangGraph
   ↓
Groq LLaMA
   ↓
AI Response
   ↓
SQLite
   ↓
React Dashboard
```

## Testing

The backend APIs can be tested using FastAPI Swagger UI 

Example webhook request:

```json
{
  "sender": "8888888888",
  "receiver": "9999999999",
  "content": "Hi, what is the price?"
}
```

The webhook processes the message, classifies the intent as `pricing`, generates an AI response through Groq LLaMA, stores the conversation, and returns the response.

## Database

SQLite is used to store:

- Message ID
- Sender
- Receiver
- Message content
- Message status
- Timestamp
- Conversation history

## WhatsApp Integration

The application is structured to work with a WhatsApp Business API provider. The WhatsApp API configuration is kept in environment variables so that provider credentials are not hard-coded into the application.

For local development and testing, incoming WhatsApp messages can also be simulated through the `/webhook` API using Swagger or Postman.

## Security

API keys and access tokens are stored in environment variables and are not hard-coded in the source code.

The `.env` file should not be committed to GitHub.

Add the following to `.gitignore`:

```
.env
venv/
__pycache__/
*.pyc
*.db
```

## Future Enhancements

- Connect and test the application with Twilio WhatsApp Sandbox
- Real-time message updates using WebSockets
- WhatsApp media message support
- Message search
- Sentiment analysis
- Human-agent fallback
- Product and order lookup
- Message templates
- Bulk messaging
