import streamlit as st
from backend import builder
from langchain_core.messages import HumanMessage, AIMessageChunk
from dotenv import load_dotenv

load_dotenv()


if 'messages_history' not in st.session_state:
    st.session_state['messages_history'] =[]

for message in st.session_state['messages_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input("Type here...")


if user_input:
    st.session_state['messages_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)



    with st.chat_message("assistant"):           
            
        config = {"configurable" : {"thread_id" :"1"}}

        ai_message = st.write_stream(
        message_chuck for message_chuck, metadata in builder.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config = config,
            stream_mode="messages"
            )
            
    )
        st.session_state['messages_history'].append({"role": "assistant", "content": ai_message})

