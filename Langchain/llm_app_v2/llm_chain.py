from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import OPENAI_API_KEY
from prompts import system_prompt


class LLMChain:
    def __init__(self):
        self.llm = ChatOpenAI()
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{input}")
        ])
        self.output_parser = StrOutputParser()
        self.chain = self.prompt | self.llm | self.output_parser

    def invoke(self, input_data):
        return self.chain.invoke({"input": input_data})
