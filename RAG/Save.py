from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm=OllamaLLM(model="llama3.2:1b")

prompt=PromptTemplate(
    input_variables=['Topic'],
    template="Give me 2 line on {Topic} "
)

chain=prompt | llm
ans=chain.invoke({'Topic':'Ms Dhoni'})
print(ans)
with open('save.txt','a') as fobj:
    fobj.write(ans + "\n")