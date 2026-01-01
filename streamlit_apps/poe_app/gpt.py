import fastapi_poe as fp

api_key='2JHnTc_6rdQbfKivEOGhZzmyb-rp0ekVKdqv47rkY_k'
message=fp.ProtocolMessage(
  role='user',
  content='Solve this math problem: ...',
  parameters={'reasoning_effort':'high'}
)

for partial in fp.get_bot_response_sync(
  messages=[message],
  bot_name='GPT-5',
  api_key=api_key
):
  print(partial)