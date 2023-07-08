```python
from django.shortcuts import render
from .models import ChatBot
from django.http import JsonResponse
import openai

# Initialize OpenAI API
openai.api_key = 'your-openai-api-key'

def train_bot(request):
    # Get all chatbot instances
    bots = ChatBot.objects.all()

    # Train each bot using OpenAI API
    for bot in bots:
        # Use OpenAI API to train the bot
        # This is a placeholder, replace with actual training code
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": bot.training_data},
            ],
        )
        bot.trained_data = response['choices'][0]['message']['content']
        bot.save()

    return JsonResponse({"message": "Bots trained successfully"})

def chat(request, bot_id):
    # Get the bot instance
    bot = ChatBot.objects.get(id=bot_id)

    # Get the message from request
    message = request.GET.get('message')

    # Use OpenAI API to generate a response
    # This is a placeholder, replace with actual response generation code
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    return JsonResponse({"response": response['choices'][0]['message']['content']})
```