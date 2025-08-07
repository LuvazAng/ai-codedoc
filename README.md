# Acerca del proyecto
**DocTech IA** es un proyecto de código abierto centrado en la generación automática de documentación técnica mediante el análisis de código fuente. Su funcionamiento se inspira en herramientas como _Deep Wiki_ y está diseñado para analizar un repositorio clonado desde su directorio raíz, recorriendo recursivamente todos sus archivos y subdirectorios.

El código del proyecto se fragmenta y se transforma en _embeddings_, que un modelo de lenguaje (LLM) utiliza para comprender el contenido del repositorio. Con esta información, el modelo genera documentación técnica precisa y coherente, estrechamente alineada con la lógica y la estructura del código.

DocTech IA será compatible con modelos LLM ejecutados localmente, como los compatibles con Ollama o LM Studio, así como con modelos accesibles mediante API, como **ChatGPT de OpenAI** o **Gemini de Google**.

El proyecto está desarrollado en **Python 3.10 o superior**.

Necesita crear un archivo `.env`.

```env
LLM_PROVIDER="ollama"
EMBEDDING_PROVIDER="ollama"

# PREDETERMINADO: Agregue esto si desea usar modelos de Ollama.
OLLAMA_BASE_URL="http://localhost:11434"
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

OLLAMA_MODEL="qwen2.5-coder:3b"
OPENAI_MODEL="YOUR_SELECTED_MODEL"
GOOGLE_MODEL="YOUR_SELECTED_MODEL"

OLLAMA_EMBEDDING_MODEL="nomic-embed-text"
OPENAI_EMBEDDING_MODEL="text-embedding-3-small"
DIMENSIÓN_EMBEDDING_DIMENSION=768

POSGRESQL_BD_NAME="SU_NOMBRE_DE_BASE_DE_DATOS_POSGRESQL"
POSGRESQL_BD_USER="SU_USUARIO_POSGRESQL"
POSGRESQL_BD_PSW="SU_CONTRASEÑA_POSGRESQL"
POSGRESQL_BD_HOST="localhost"
POSGRESQL_BD_PORT="5432"

# CLONACIÓN DE ENTORNO
GITHUB_TOKEN="SU_TOKEN_GITHUB"
```