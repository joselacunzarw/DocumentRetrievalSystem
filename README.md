
# Document Retrieval System

## Descripción

Este proyecto implementa un sistema para la recuperación de documentos relevantes basado en consultas utilizando técnicas avanzadas de recuperación de información y modelos de lenguaje. El sistema permite a los usuarios enviar una pregunta y recibir documentos relevantes en respuesta.

## Estructura del Proyecto

- `a_env_vars.py`: Archivo que contiene las variables de entorno utilizadas en el proyecto.
- `app.py`: Define la aplicación Flask y el endpoint para recibir y procesar las consultas.
- `core.py`: Script principal que contiene las funciones para cargar, dividir y almacenar documentos en una base de datos vectorial.
- `README.md`: Proporciona una descripción general del proyecto y guía para su uso.

## Dependencias

El proyecto utiliza las siguientes bibliotecas de Python:

- `flask`
- `langchain`
- `chroma`

Puedes instalar las dependencias utilizando el archivo `requirements.txt` proporcionado. Para ello, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias necesarias:

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt
```

## Configuración

Configura las variables de entorno en el archivo `a_env_vars.py`:

```python
OPENAI_API_KEY = 'tu-api-key-aqui'
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
DATA_PATH = r"ruta/a/tus/datos"
CHROMA_PATH = r"ruta/a/tu/repositorio/chroma"
```

## Uso

Para iniciar la aplicación Flask, ejecuta el siguiente comando:

```bash
python app.py
```

### Endpoint

- **POST `/recuperar_documentos`**

#### Descripción:
Recibe una pregunta en formato JSON y devuelve los documentos relevantes.

#### Ejemplo de Solicitud:
```sh
curl -X POST -H "Content-Type: application/json" -d '{"question": "¿Cuál es el capital de Francia?"}' http://localhost:5000/recuperar_documentos
```

#### Ejemplo de Respuesta:
```json
{
  "documents": [
    {
      "metadata": {
        "title": "París",
        "content": "París es la capital de Francia...",
        ...
      }
    },
    ...
  ]
}
```

## Ejemplo de Contenido

### a_env_vars.py

```python
# a_env_vars.py

# Clave API de OpenAI - Considera almacenarla en un archivo .env para mayor seguridad

# Nombre del modelo de incrustación utilizado
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Ruta a los datos
DATA_PATH = r"C:\Users\josel\OneDrive\Documents\Desktop\repo"

# Ruta al repositorio de Chroma
CHROMA_PATH = r"C:\implementacion de RAG\2 - Almacen de documentos\Repositorio\chroma"
```

### core.py

```python
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
```

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Contacto

Para preguntas o soporte, contacta a [tu-email@dominio.com](mailto:tu-email@dominio.com).
