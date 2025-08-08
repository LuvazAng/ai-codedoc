from src.llm.base_provider import BaseProviderService
import ollama
from config.conf import OLLAMA_MODEL


class OllamaProviderService(BaseProviderService):

    def __init__(self, logger):
        super().__init__(logger)
        self.logger = logger

    def generate_text(self, content: str) -> str:
        try:
            response_generate = ollama.generate(
                model=OLLAMA_MODEL,
                prompt=content,
                options={
                    "temperature": 0.0,
                },
            )
            return response_generate["response"]
        except Exception as e:
            self.logger.error(f"Error generating text with Ollama: {e}")
            return None

    def generate_embeddings(self, content):
        pass
