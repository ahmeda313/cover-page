from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def generate_insights(document):
    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(document)


    # Generate embeddings for chunks and create FAISS index
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    faiss_index = FAISS.from_texts(chunks, embeddings)
    


    # Build a RetrievalQA chain
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    context = ''' You are an expert assistant tasked with answering questions 
            based on the most relevant context provided. Use the following pieces of 
            context to answer the question as precisely and shortly as possible.'''


    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=faiss_index.as_retriever(),

    )

    result = []
    def ask_question(query):
        response = qa_chain.invoke(query)
        return response['result']


    result.append(ask_question(context+"What are the key points discussed in the document?"))
    result.append(ask_question(context+"Who wrote the document?"))
    result.append(ask_question(context+"Who is the document intended for?"))

    return result
