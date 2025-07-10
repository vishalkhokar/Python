from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate

LLM=OllamaLLM(model='llama3.2:1b')

temp=PromptTemplate(
    template='Give me information about {person}'
)

userin=input()
res=temp.format(person=userin)
ans=LLM.invoke(res)
print(ans)