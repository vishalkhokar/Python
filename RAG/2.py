from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
users_json = response.json()
json_text = json.dumps(users_json, indent=2)

llm = OllamaLLM(model="mistral:latest")

prompt = PromptTemplate.from_template("""
You are an expert API tester. Analyze the following JSON data, which represents a list of users from a REST API and give me 3 test cases on it .

JSON:
{json_data}
""")

# Step 4: Run chain
chain: Runnable = prompt | llm
result = chain.invoke({"json_data": json_text})
print(result)
