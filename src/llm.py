import os
from groq import Groq
from src.prompt import system_instruction

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": system_instruction,
    },
    ]

def ask_order(messages,model="llama3-8b-8192",temperature = 0):
# Create a chat completion
    response = client.chat.completions.create(
        model = model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content
