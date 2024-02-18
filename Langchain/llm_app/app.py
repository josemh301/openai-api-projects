import streamlit as st
from llm_chain import LLMChain

def main():
    st.title("LLM Web App")
    st.write("Welcome to the LLM Web App!")

    # LLM Options
    st.subheader("LLM Options")
    llm_options = ["Option 1", "Option 2", "Option 3"]
    selected_option = st.selectbox("Select an option", llm_options)

    # File Uploader
    # uploaded_file = st.file_uploader("Upload a PDF file")

    # User Input
    user_input = st.text_area("What is your question")

    # Invoke LLM Chain
    llm_chain = LLMChain()
    response = llm_chain.invoke(user_input)
    st.write(response)

    # if uploaded_file is not None:
    #     st.write("File uploaded successfully!")

    print(user_input)

if __name__ == "__main__":
    main()
