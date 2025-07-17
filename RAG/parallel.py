from langchain_ollama.llms import OllamaLLM
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnableParallel

llm=OllamaLLM(model="llama3.2:1b")
videoid="4cS3yT4iF2E"
try:
    transcript_list=YouTubeTranscriptApi.get_transcript(videoid,languages=["en"])
    
    transcript=" ".join(chunk["text"] for chunk in transcript_list)
    #print(transcript)
except TranscriptsDisabled:
    print("No Caption available")
    
splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks=splitter.create_documents([transcript])
print(len(chunks))

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store=FAISS.from_documents(chunks,embedding)
#print(vector_store.index_to_docstore_id)


retriever=vector_store.as_retriever(search_type="similarity", search_kwargs={"k":4})

question="Give me the summary of the content"
ans=retriever.invoke(question)
context="\n\n".join(doc.page_content for doc in ans)
print(context)

summary_prompt=PromptTemplate(
    template="Summarize the context:\n {context}",
    input_variables=["context"]
)
keyword_prompt=PromptTemplate(
    template="Extarct the important keyword from the the {context}",
    input_variables=["context"]
)
sentiment_prompts=PromptTemplate(
    template="What is the overall sentiment of context (Positive,Neutral,Negative) ? \n{context}",
    input_variables=["context"]
)

summary_chain=summary_prompt | llm 
keyword_chain=keyword_prompt | llm
sentiment_chain=sentiment_prompts | llm

parallel=RunnableParallel (
    summ=summary_chain,
    keyws=keyword_chain,
    senti=sentiment_chain
)

output=parallel.invoke({"context":context})
print(output)