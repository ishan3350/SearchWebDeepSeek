import search
from ollama import chat

prompt = search.ask_user()

print(prompt)

response = chat(
    model='deepseek-r1:8b',
    messages=[
        {'role': 'user', 'content': prompt}
    ]
)

print(response.message.content)