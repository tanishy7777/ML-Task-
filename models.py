import os
from groq import Groq
import backoff 
# gives us decorators to wrap around functions => so that func retried until success/some 
# condition is met

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_chat_completion(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

print(get_chat_completion("Explain the importance of fast language models"))

