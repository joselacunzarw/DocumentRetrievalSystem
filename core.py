# core.py

import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  # Importar embeddings de HuggingFace de Langchain
import a_env_vars  # Importar módulo para manejar variables de entorno
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain import hub
from langchain_core.prompts import PromptTemplate


# Configuración de variables globales
EMBEDDING_MODEL_NAME = a_env_vars.EMBEDDING_MODEL_NAME
DATA_PATH = a_env_vars.DATA_PATH
CHROMA_PATH = a_env_vars.CHROMA_PATH
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# Inicialización de la base de datos Chroma y el modelo de incrustación
#db = Chroma(persist_directory=CHROMA_PATH, embedding_function=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME))
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
llm = ChatOpenAI(model="gpt-4o-mini")
prompt = hub.pull("rlm/rag-prompt")

def recuperar_documentos(query):
    """
    Recupera documentos relevantes en base a la consulta proporcionada.
    
    :param query: Consulta en formato de texto.
    :return: Lista de documentos relevantes.
    """
    try:
        docs = retriever.invoke(query)
        # Imprime los metadatos de los documentos recuperados para depuración
        for documento in docs:
            print(documento.metadata)
        return docs
    except Exception as e:
        print(f"Error al recuperar documentos: {e}")
        return []


def consultar_llm(context, question):
    print("llego aca")
    context = context
    question=question
    from langchain_core.prompts import PromptTemplate
    template = "Eres un asistente, con el contexto que te doy, respodne la pregunta contexto    : " +str(context) + " question: "+question


    print("creo el temp")
    
    from langchain_core.output_parsers import StrOutputParser
    result = llm.invoke(template)
    #parser = StrOutputParser(result)
    print (result.content)
    return result.content
    
