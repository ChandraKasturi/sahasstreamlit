from openai import OpenAI
import requests
import json
import streamlit as st
import time


def gen():
    for i in json.loads(stream.text)["message"]:
        time.sleep(0.01)
        yield i
       
st.set_page_config(
        page_title="FNO User Guide",
        page_icon="computer"
       
    )

st.title("FNO User Guide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
    

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = requests.post('http://localhost:7000/chat/standalone', json={"message": prompt})
        response = st.write_stream(gen)
    st.session_state.messages.append({"role": "assistant", "content": response})
  