API Documentation

The backend is built using FastAPI and provides REST APIs for sending, receiving, retrieving, and updating WhatsApp messages.

Base URL

http://127.0.0.1:8000

Interactive API documentation is available at:

http://127.0.0.1:8000/docs

---

1. Send Message

POST "/send-message"

Sends a message to a receiver and stores the message in the SQLite database.

Request Body

{
  "sender": "919876543210",
  "receiver": "918765432109",
  "content": "Hello, how can I help you?",
  "status": "sent"
}

Response

{
  "id": 1,
  "sender": "919876543210",
  "receiver": "918765432109",
  "content": "Hello, how can I help you?",
  "status": "sent"
}

---

2. Get All Messages

GET "/messages"

Returns all messages stored in the SQLite database.

Response

[
  {
    "id": 1,
    "sender": "919876543210",
    "receiver": "918765432109",
    "content": "Hello",
    "status": "sent"
  }
]

---

3. Get Messages by Phone Number

GET "/messages/{phone}"

Returns all messages where the specified phone number is either the sender or receiver.

Example

GET /messages/918765432109

Response

[
  {
    "id": 1,
    "sender": "919876543210",
    "receiver": "918765432109",
    "content": "Hello",
    "status": "sent"
  }
]

If no messages are found, the API returns:

{
  "detail": "No messages found for this phone number"
}

---

4. Receive Incoming Message

POST "/webhook"

Receives an incoming message and processes it through the AI workflow.

The webhook supports:

- Text messages
- Location messages
- Contact messages

Text Message Example

{
  "sender": "918765432109",
  "content": "What is the price?"
}

The message is processed by the LangGraph workflow:

Incoming Message
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

Location Message

Location information is received using latitude and longitude.

Example:

Location received:
latitude=12.9716
longitude=77.5946

Contact Message

Contact information is received using the contact name and phone number.

Example:

Contact received:
name=Akhila
phone=918765432109

---

5. Update Message Status

PATCH "/messages/{message_id}/status"

Updates the delivery status of a stored message.

Supported statuses:

sent
delivered
read

Example

PATCH /messages/1/status

Request:

read

Response

{
  "id": 1,
  "sender": "919876543210",
  "receiver": "918765432109",
  "content": "Hello",
  "status": "read"
}

---

Error Handling

The API uses appropriate HTTP status codes for errors.

Status Code| Meaning
200| Request successful
201| Resource created
404| Resource not found
422| Validation error
500| Internal server error
502| External WhatsApp service error

FastAPI and Pydantic are used for request validation, while database errors are handled using appropriate exception handling and transaction rollback.

---

API Testing

The APIs can be tested using:

- FastAPI Swagger UI
- Postman

Swagger UI provides an interactive interface for sending requests and viewing API responses.

http://127.0.0.1:8000/docs