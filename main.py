import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key
# streamlit frameowrk
st.title('Grammar Bot')
input_text = st.text_input("Input a piece of text")


first_input_prompt = PromptTemplate(
    input_variables=['passage'],
    template="Fix the grammar issue in {passage}"
)

# OPENAI LLMS
llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))
