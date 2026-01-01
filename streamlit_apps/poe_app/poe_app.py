import os, openai 

client = openai.OpenAI(
  # api_key=os.getenv('2JHnTc_6rdQbfKivEOGhZzmyb-rp0ekVKdqv47rkY_k'), # https://poe.com/api_key
  api_key=os.getenv("POE_API_KEY"),
  base_url='https://api.poe.com/v1',
)

chat = client.chat.completion.create(
  model='Claude-Opus-4.1',  # or other models (Claude-Sonnet-4, Gemini-2.5-Pro, Llama-3.1-405B, Grok-4..)
  messages=[{'role': 'user', 'content': 'Top 3 things to do in Edmonton?'}],
)

print(chat.choices[0].message.content)