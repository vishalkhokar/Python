from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

template1=PromptTemplate(
    input_variables=['topic'],
    template='Write a Joke about {topic}'
)

template2=PromptTemplate(
    input_variables=['response'],
    template='explain the following Joke {response}'
)
ratingtemplate=PromptTemplate(
    input_variables=['joke'],
    template='Rate the  Joke {joke} on the following scale of 1 to 5'
)
llm=OllamaLLM(model='llama3:8b')

parser=StrOutputParser()

joke_chain=template1 | llm | parser

user_input=input()

joke=joke_chain.invoke({'topic':user_input})
print(joke)

convert_to_dict=RunnableLambda(lambda joke:{"response":joke})

final_chain= joke_chain | convert_to_dict | template2 | llm | parser

result=final_chain.invoke({'topic':user_input})
print(result)


rate= ratingtemplate| llm | parser
revie=rate.invoke ({'joke':joke})
print(revie)