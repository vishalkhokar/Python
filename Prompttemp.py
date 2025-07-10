from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm=OllamaLLM(model='llama3.2:1b')

xyz=PromptTemplate.from_template("What is the capital of {country}")

prompt=xyz.format(country="India")
print(prompt)
response=llm.invoke(prompt)
print("LLM says",response)