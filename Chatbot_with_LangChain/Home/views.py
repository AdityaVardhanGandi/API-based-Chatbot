from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')

def home(request):
    return render(request, "home.html")

def chat(request):
    return render(request, "chat.html")

def about(request):
    return render(request, "about.html")

def chatAPI(request):
    if request.method == "POST":
        try:
            # Get the prompt from POST data
            prompt = request.POST.get("prompt", "")
            
            if not prompt:
                return JsonResponse({"error": "No prompt provided"}, status=400)
            
            # Check if API key is configured
            if not os.getenv("GEMINI_API_KEY"):
                return JsonResponse({"error": "Gemini API key not configured"}, status=500)
            
            # Make API call to Gemini
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1024,
                    top_p=0.8,
                    top_k=40
                )
            )
            
            # --- Gemini API finish_reason 2 fix ---
            response_text = getattr(response, "text", None)
            if not response_text or not response_text.strip():
                return JsonResponse({
                    "choices": [{"text": ""}],
                    "error": "No response generated. Please try rephrasing your question."
                })
            
            # Extract the response text
            response_text = response.text
            
            # Return in the format expected by your frontend
            return JsonResponse({
                "choices": [{"text": response_text}]
            })
            
        except Exception as e:
            print(f"Error: {str(e)}")  # For debugging
            return JsonResponse({"error": f"API Error: {str(e)}"}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)