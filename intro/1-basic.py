import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
         "role": "user", 
         "content": "write a haiku about ai"
        }
    ]
)

response = completion.choices[0].message.content
print(response)
