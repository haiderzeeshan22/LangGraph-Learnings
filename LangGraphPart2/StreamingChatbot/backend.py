# from typing_extensions import TypedDict, Annotated
# from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage, BaseMessage
# from langchain_ollama import ChatOllama

# from langgraph.graph.message import add_messages
# from langgraph.checkpoint.memory import InMemorySaver
# from langgraph.graph import StateGraph, START, END

# model = ChatOllama(model="phi3:latest", temperature=0.9)

# class ChatState(TypedDict):
#     messages : Annotated[list[BaseMessage], add_messages]


# def chatbot(state:ChatState):
#     messages = state["messages"]

#     response = model.invoke(messages)

#     return {"messages" : [response]}

# graph = StateGraph(ChatState)
# graph.add_node("chatbot", chatbot)

# graph.add_edge(START, "chatbot")
# graph.add_edge("chatbot", END)

# memory = InMemorySaver()
# builder = graph.compile(checkpointer=memory)


from typing import Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, BaseMessage

from langgraph.graph import StateGraph, START , END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatOllama(model="phi3:latest", temperature=0.9)



class ChatState(TypedDict):
    messages :Annotated[list[BaseMessage], add_messages]


def chatbot(state:ChatState ):
    messages = state['messages']

    response = model.invoke(messages)

    return {"messages": [response]}



graph = StateGraph(ChatState)

graph.add_node('chatbot', chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

memory = InMemorySaver()
builder = graph.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "Zeeshan_Chat"
    }
}



# while True :
#     user_input = input("You: ")
#     if user_input.strip().lower() in ["exit", "bye"]:
#         print("GoodBye")
#         break
#     response = builder.invoke({
#         "messages": [HumanMessage(content=user_input)]
#     }, config)

#     print("user: ", user_input, "\n", "AI: ", response['messages'][-1].content)


