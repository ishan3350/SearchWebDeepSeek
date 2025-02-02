import search
from ollama import chat

# starting the script by asking user for their query or question
prompt = search.ask_user()

#asking question to DeepSeek model running on Ollama server
response = chat(
    model='deepseek-r1:8b',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

# Show the response from DeepSeek
print(response.message.content)