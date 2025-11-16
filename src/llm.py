from groq import Groq
from src.prompt import system_prompt

client = Groq()

messages = [
    {"role": "system", "content": system_prompt}
]

def ask_order(messages, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.4
    )
    return response.choices[0].message.content
