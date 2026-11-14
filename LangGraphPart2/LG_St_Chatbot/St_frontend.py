import streamlit as st
from LG_backend import builder
from langchain_core.messages import HumanMessage


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
# message_history = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# with st.chat_message("user"):
#     st.text("Hi")

# with st.chat_message("assistant"):
#     st.text("Hello")

# with st.chat_message("user"):
#     st.text("My name is nitish")

user_input = st.chat_input("Type here...")

# if user_input:
#     message_history.append({'role': "user", "content": user_input})
#     with st.chat_message("user"):
#         st.text(user_input)

# if user_input:
#     message_history.append({'role': "assistant", "content": user_input})
#     with st.chat_message("assistant"):
#         st.text(user_input)

if user_input:
    
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    config = {"configurable":{"thread_id": "Zeeshan_Chat"}} # this line was written which raised the next problem -> ValueError: Checkpointer requires one or more of the following 'configurable' keys: thread_id, checkpoint_ns, checkpoint_id

    response = builder.invoke({"messages": [HumanMessage(content=user_input)]}, config)
    ai_message = response['messages'][-1].content


    st.session_state['message_history'].append({"role":"user", "content": user_input})
    with st.chat_message("assitnant"):
        st.text(ai_message)