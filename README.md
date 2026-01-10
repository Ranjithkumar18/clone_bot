# ChatGPT Clone

A Django-based ChatGPT clone application using Groq API for AI responses.

## Features

- Modern, ChatGPT-like user interface
- Real-time chat with AI responses
- Conversation history management
- Responsive design
- Environment variable configuration

## Setup Instructions

1. **Create a virtual environment** (if not already created):
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - Windows (PowerShell):
     ```powershell
     & .\venv\Scripts\Activate.ps1
     ```
     or
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
     **Note:** If you get an execution policy error, run:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   - Windows (CMD):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your Groq API key and optionally specify a model:
     ```
     SECRET_KEY=django-insecure-(cedq@@ah*fzkjz4t@fh5w^zu7v*wporz@3=%e2!w+)sdrr_y1
     GROQ_API_KEY=your_actual_groq_api_key_here
     GROQ_MODEL=llama-3.1-8b-instant
     ```
   - You can get a Groq API key from: https://console.groq.com/
   - Available models: `llama-3.1-8b-instant` (default, fast), `llama-3.1-70b-versatile` (if available), `mixtral-8x7b-32768`

5. **Run migrations** (if needed):
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Authentication

The application requires user authentication to access the chat interface.

### First Time Setup

1. **Sign Up**: Navigate to `/signup/` to create a new account
   - Username: At least 3 characters
   - Password: At least 8 characters, must contain letters and numbers
   - Confirm Password: Must match the password

2. **Login**: After signing up, you'll be automatically logged in. For future sessions, use `/login/`

### Password Requirements

- Minimum 8 characters
- Must contain at least one letter
- Must contain at least one number

## Usage

1. **Login or Sign Up** to access the chat interface
2. Type your message in the input box
3. Press Enter or click the Send button
4. Wait for the AI response
5. Continue the conversation!
6. Use the **Logout** button in the header to sign out

## Project Structure

```
Chatgpt_clone/
├── chat/                 # Main chat application
│   ├── views.py         # View functions
│   ├── urls.py          # URL routing
│   └── ...
├── chatgpt_clone/       # Django project settings
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   └── ...
├── templates/           # HTML templates
│   └── chat/
│       └── index.html   # Main chat interface
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
└── manage.py           # Django management script
```

## Notes

- Make sure to keep your `.env` file secure and never commit it to version control
- The application uses Groq's `llama-3.1-8b-instant` model by default (fast and reliable)
- You can change the model by setting `GROQ_MODEL` in your `.env` file
- If a model is decommissioned, check https://console.groq.com/docs/models for available models

