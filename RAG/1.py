from langchain_ollama.llms import OllamaLLM
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters.character import RecursiveCharacterTextSplitter


llm=OllamaLLM(model="llama3.2:1b")
videoid="Gfr50f6ZBvo"
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

res=retriever.invoke("What is deepmind")

prompt=PromptTemplate(
    template=""" You are helpfull assistant Answer only from the provided transcipt  context
    if the context is insufficient,just say You dont know
    {context}
    Question :{question}
    """,
    input_variables=['context','question']
)

question ="is the topic of Superman disccussed in this video? if yes then what was discussed"
retrieved_docs=retriever.invoke(question)

ans="\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt=prompt.invoke({"context":ans,"question":question})
finalans=llm.invoke(final_prompt)
print(ans)
