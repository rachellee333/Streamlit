import fastapi_poe as fp
import streamlit as st

api_key="2JHnTc_6rdQbfKivEOGhZzmyb-rp0ekVKdqv47rkY_k"
message=fp.ProtocolMessage(
  role="user",
  content="Explain how to land a job as a data scientist",
  parameters={"thinking_budget": 12288}
)

for partial in fp.get_bot_response_sync(messages=[message], bot_name='Claude-Sonnet-4.5', api_key=api_key):
  # print(partial)
  st.write(partial)
  # st.write(message.content['text'])