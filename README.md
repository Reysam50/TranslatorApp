# 🌍 PolyLingo Translator

A full-stack language translation web application built with Flask, JavaScript, HTML, and CSS. The application allows users to translate text between multiple languages using a self-hosted LibreTranslate API running on a Linux VPS.

![alt text](<Screenshot 2026-06-06 104445.png>)

## 📖 Overview

PolyLingo Translator is a web-based translation platform designed to provide fast and accessible language translation through a modern and responsive user interface.

Unlike many translation applications that rely directly on commercial APIs, PolyLingo Translator uses a self-hosted LibreTranslate instance deployed on a Linux VPS. The Flask backend acts as a middleware layer between the frontend and the translation service, allowing for future expansion to support multiple translation engines and providers.

This project demonstrates practical skills in:

* Python development
* Flask web development
* REST API integration
* JSON processing
* Linux server administration
* Frontend development
* Client-server architecture
* VPS deployment
* Reverse proxy configuration

---

## 🚀 Features

### Core Features

* Translate text between multiple languages
* Dynamic language loading from translation server
* Responsive user interface
* Real-time translation requests
* Self-hosted translation engine

### User Experience Features

* Copy translated text to clipboard
* Text-to-Speech (TTS) support
* Loading indicators during translation
* Error handling and user feedback
* Mobile-friendly design

### Backend Features

* Flask API integration
* JSON request and response handling
* External API communication
* Modular project structure
* Translation service abstraction

---

## 🏗️ System Architecture

```text
User Browser
      │
      ▼
HTML / CSS / JavaScript
      │
      ▼
Flask Backend
      │
      ▼
HTTP Requests
      │
      ▼
LibreTranslate API
(Linux VPS)
      │
      ▼
Translation Engine
      │
      ▼
JSON Response
      │
      ▼
Flask Backend
      │
      ▼
Browser Interface
```

---

## 📂 Project Structure


PolyLingo-Translator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── venv/
```

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* Requests

### Frontend

* HTML5
* CSS3
* JavaScript

### Infrastructure

* Linux VPS
* LibreTranslate
* Nginx Reverse Proxy
* systemd Service Manager

### Data Format

* JSON

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/polylingo-translator.git
cd polylingo-translator
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Translation Server

Open:

```python
BASE_URL = "http://YOUR_VPS_IP"
```

Replace with your LibreTranslate server address.

### 5. Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### Home Page

```http
GET /
```

Returns the main application interface.

---

### Supported Languages

```http
GET /languages
```

Returns all supported translation languages.

Example Response:

```json
[
  {
    "code": "en",
    "name": "English"
  },
  {
    "code": "fr",
    "name": "French"
  }
]
```

---

### Translate Text

```http
POST /translate
```

Request:

```json
{
  "text": "Hello World",
  "source": "en",
  "target": "fr"
}
```

Response:

```json
{
  "translatedText": "Bonjour le monde"
}
```

---

## 📋 Skills Demonstrated

This project demonstrates:

* Python Programming
* Flask Development
* REST API Consumption
* JSON Processing
* HTTP Requests and Responses
* Client-Server Communication
* Linux Administration
* VPS Management
* Reverse Proxy Configuration
* Frontend Development
* Responsive Web Design
* Error Handling
* System Architecture Design

---

## 🔮 Future Enhancements

Planned improvements include:

* Translation history
* User authentication
* Translation caching
* Automatic language detection
* Multi-engine translation routing
* Translation analytics
* Dark/Light mode
* Docker containerization
* CI/CD pipeline integration
* Database support
* Rate limiting

---

## 📸 Screenshots

Add screenshots of the application here.

### Home Screen

```text
Screenshot Placeholder
```

### Translation Example

```text
Screenshot Placeholder
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📄 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**Lyson Reysam Mbughi**

Computer Network Engineering Student
University of Malawi (UNIMA)

GitHub: https://github.com/Reysam50

Portfolio: https://lyson-reysam-mbughi-portifolio-webs.vercel.app

LinkedIn: www.linkedin.com/in/lyson-mbughi-455743353
