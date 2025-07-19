# Django Chatbot with Google Gemini AI

A modern web-based chatbot application built with Django framework, featuring Google's Gemini AI for intelligent conversational responses. This project provides a clean, responsive interface for users to interact with AI through a web browser.

## 🚀 Features

- **AI-Powered Conversations**: Integrated with Google Gemini 2.5 Flash model for intelligent responses
- **Modern Web Interface**: Clean, responsive design optimized for user experience
- **RESTful API**: JSON API endpoint for external integrations and mobile apps
- **Multi-page Application**: Complete web application with home, chat, and about pages
- **Real-time Chat**: Fast, dynamic chat interactions with error handling
- **Configurable Settings**: Easy setup with environment variables
- **Cross-platform**: Works on desktop, tablet, and mobile devices

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **AI Model**: Google Gemini 2.5 Flash
- **Database**: SQLite (easily configurable to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Chatbot
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv chatbot_env

# Activate virtual environment
# On Windows:
chatbot_env\Scripts\activate
# On macOS/Linux:
source chatbot_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory (same level as `manage.py`):

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

**⚠️ IMPORTANT**: You must obtain a Gemini API key from Google AI Studio:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and paste it in your `.env` file

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🎯 How to Use

### Web Interface

1. **Home Page**: Navigate to `http://127.0.0.1:8000/` to access the landing page
2. **Chat Page**: Click on "Chat" or navigate to `http://127.0.0.1:8000/chat/` to start chatting
3. **About Page**: Visit `http://127.0.0.1:8000/about/` for more information

### API Endpoint

The chatbot also provides a RESTful API endpoint for programmatic access:

**Endpoint**: `POST /api`

**Request Format**:
```bash
curl -X POST http://127.0.0.1:8000/api \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "prompt=Hello, how are you?"
```

**Response Format**:
```json
{
  "choices": [
    {
      "text": "Hello! I'm doing well, thank you for asking. How can I help you today?"
    }
  ]
}
```

**Error Response**:
```json
{
  "error": "Error message here"
}
```

## 📁 Project Structure

```
Chatbot/
├── Chatbot/                 # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── Chatbot_V1/              # Django app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py              # App URL patterns
│   └── views.py             # View functions
├── templates/               # HTML templates
├── .env                     # Environment variables (create this)
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory with:

```env
# Required: Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Django settings
DEBUG=True
SECRET_KEY=your_secret_key_here
```

### Gemini Model Configuration

The chatbot uses the following Gemini configuration (in `views.py`):
- **Model**: `gemini-2.5-flash`
- **Temperature**: 0.7 (creativity level)
- **Max Output Tokens**: 1024
- **Top P**: 0.8
- **Top K**: 40

You can modify these parameters in the `chatAPI` function within `Chatbot_V1/views.py`.

## 🚀 Deployment

### For Production:

1. **Update Settings**: Set `DEBUG=False` in settings.py
2. **Environment Variables**: Use proper environment variable management
3. **Database**: Consider using PostgreSQL or MySQL for production
4. **Static Files**: Configure static file serving
5. **Security**: Update `SECRET_KEY` and `ALLOWED_HOSTS`

### Deployment Options:
- **Heroku**: Easy deployment with Heroku CLI
- **AWS**: Deploy using EC2, Elastic Beanstalk, or Lambda
- **DigitalOcean**: App Platform or Droplets
- **Railway**: Simple deployment platform
- **Vercel/Netlify**: For serverless deployment

## 🐛 Troubleshooting

### Common Issues:

1. **API Key Not Working**:
   - Ensure your `.env` file is in the correct location (same level as `manage.py`)
   - Verify the API key is correct and active
   - Check if you have billing enabled for your Google Cloud project

2. **Empty Responses**:
   - This is handled by the application with proper error messages
   - Try rephrasing your question if you get empty responses

3. **Django Errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Run migrations: `python manage.py migrate`
   - Check if the virtual environment is activated

4. **Port Already in Use**:
   - Use a different port: `python manage.py runserver 8080`
   - Or find and stop the process using port 8000

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is open source. Please check the repository for license details.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue in the repository
3. Contact the maintainer

## 🔗 Links

- [Google Gemini API Documentation](https://developers.generativeai.google/api/rest)
- [Django Documentation](https://docs.djangoproject.com/)
- [Google AI Studio](https://makersuite.google.com/app/apikey) (for API keys)

---

**Remember**: Always keep your API keys secure and never commit them to version control!
