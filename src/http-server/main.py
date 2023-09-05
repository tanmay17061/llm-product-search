from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import Chroma
from langchain.embeddings.fake import DeterministicFakeEmbedding

class Query(BaseModel):
    text: str

app = FastAPI()
db = Chroma(persist_directory="data/db.chroma",embedding_function=DeterministicFakeEmbedding(size=100))

@app.post("/")
async def query_handler(q: Query):
    docs = db.similarity_search(q.text)
    # return docs[0].page_content
    return {"message": "Most relevant document:" + docs[0].page_content}