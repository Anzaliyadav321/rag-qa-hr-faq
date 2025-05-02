from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from app.utils import clean_response, final_response_logic
import os


# path to faiss_index from project root
faiss_path = os.path.join(os.path.dirname(__file__), "..", "notebooks", "faiss_index")

# Load vector store
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local(
    faiss_path,
    embedding_function,
    allow_dangerous_deserialization=True  
)
retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})

# Define LLM and prompt
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-32B",
    task="text-generation",
    temperature=0.8,
    max_new_tokens=250
)


model = ChatHuggingFace(llm=llm)

prompt_template = PromptTemplate(
    template="""
You are a helpful assistant.
Answer only from the provided context.
If the context is insufficient, say "I don't know".

context: {retrieved_text}
Question: {user_question}
""",
    input_variables=["retrieved_text", "user_question"]
)

def run_qa_pipeline(question):
    docs = retriever.invoke(question)
    retrieved_text = "\n\n".join(doc.page_content for doc in docs)
    prompt = prompt_template.invoke({"retrieved_text": retrieved_text, "user_question": question}).text
    raw_response = model.invoke([HumanMessage(content=prompt)]).content.strip()
    cleaned = clean_response(raw_response)
    final = final_response_logic(cleaned)
    return final
