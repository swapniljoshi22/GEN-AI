from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

template1= PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2= PromptTemplate(
    template="Write a summary on the following text. /n {text}",
    input_variables=['text']
)

# without using stroutputparser
prompt1 = template1.invoke({'topic':"Machine Learning"})
result1 = model.invoke(prompt1)

prompt2 = template1.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

print(result2.content)

# with using stroutputparser and chains

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Machine Learning'})

print(result)