# core.py

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings  # Importar embeddings de HuggingFace de Langchain
import a_env_vars  # Importar módulo para manejar variables de entorno

# Configuración de variables globales
EMBEDDING_MODEL_NAME = a_env_vars.EMBEDDING_MODEL_NAME
DATA_PATH = a_env_vars.DATA_PATH
CHROMA_PATH = a_env_vars.CHROMA_PATH

# Inicialización de la base de datos Chroma y el modelo de incrustación
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME))
retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.4})

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

