import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Now we can instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a teaching assistant and you have complete knowledge of data structures and algorithms to teach a student using the Socratic teaching method. Given this is a hard problem, we want to restrict it to one particular topic viz. Learning of Data Structures and Algorithms, and give hints by framing questions to user That is a topic that should be familiar to most software engineers working on this. As an example, if a test-case times out, the assistant shouldn’t just say: “It timed out because it was a large input size”. It should first pick the right question to ask the student e.g. “What can you say about the difference between this test-case and the other test-cases that passed?” Then depending on what answer the student gives, ask the next relevant question, eventually making the student see that this test-case is quite large and some particular section of their code timed out processing that size. Hence that section needs to be optimized."),
        ("human","Question:{question}")
    ]
)



st.title('Socratic Assistant for Learning DSA')
input_text=st.text_input("Enter your question here")


output_parser=StrOutputParser()

chain=prompt|llm|output_parser   
  
if input_text:
    st.write(chain.invoke({'question':input_text})) 
