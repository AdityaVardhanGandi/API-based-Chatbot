"""
URL configuration for Chatbot_with_LangChain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Chatbot_V1.views import chat, about, chatAPI, home

urlpatterns = [
    path('', home, name='Home'),
    path('home', home, name='Home'),           # Home page (landing page)
    path('chat/', chat, name='chat'),      # Chat page (chat.html)
    path('about/', about, name='about'),   # About page
    path('api', chatAPI, name='chatAPI'), # API endpoint for chat
]
