from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser



#######################################################3

import streamlit as st

st.title("LLM Web App")
st.write("Welcome to the LLM Web App!")

# Add your LLM functionality here

# Add a subtitle
st.subheader("LLM Options")

# Add a dropdown menu
llm_options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Select an option", llm_options)

# Add a file uploader
uploaded_file = st.file_uploader("Upload a PDF file")

# Add a text area
user_input = st.text_area("What is your question")

response = chain.invoke({"input": user_input})

st.write(response)

if uploaded_file is not None:
    # Process the uploaded file
    st.write("File uploaded successfully!")

print(user_input)


