import os, openai
import fastapi_poe as fp
import streamlit as st

st.balloons()
my_list = []
my_string = ''
# botName = 'Claude-Sonnet-bot.5'
# botName = 'gpt-5-nano'
botName = 'gemini-3-flash'

system_message_default = 'Think of an inspiring quote'

system_message = st.text_area(
  f'Enter a system message to instruct Open AI. This bot is using the {botName} model', system_message_default
)

analyze_button = st.button('Analyze Text')
if analyze_button:
  api_key="2JHnTc_6rdQbfKivEOGhZzmyb-rp0ekVKdqv47rkY_k"
  message=fp.ProtocolMessage(
    role="user",
    content=system_message,
    parameters={"thinking_budget": 12288}
  )

  for partial in fp.get_bot_response_sync(messages=[message], bot_name=botName, api_key=api_key):
    my_list.append(partial.text)
    
  complete_response = ''.join(my_list)

  st.write(complete_response)