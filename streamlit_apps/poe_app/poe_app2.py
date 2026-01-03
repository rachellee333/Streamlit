import os, openai
import fastapi_poe as fp
import streamlit as st

st.balloons()

system_message_default = 'Think of an inspiring quote'

system_message = st.text_area(
  'Enter a system message to instruct Poe AI', system_message_default
)

analyze_button = st.button('Analyze Text')
if analyze_button:
  api_key="2JHnTc_6rdQbfKivEOGhZzmyb-rp0ekVKdqv47rkY_k"
  message=fp.ProtocolMessage(
    role="user",
    content=system_message,
    parameters={"thinking_budget": 12288}
  )

  for partial in fp.get_bot_response_sync(messages=[message], bot_name='Claude-Sonnet-4.5', api_key=api_key):
    st.write(partial.text)