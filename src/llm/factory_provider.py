from src.llm.providers.gemini_provider import GeminiProviderService
from src.llm.providers.ollama_provider import OllamaProviderService
from src.llm.providers.openai_provider import OpenAIProviderService
from config.conf import EMBEDDING_PROVIDER, LLM_PROVIDER


class ProviderFactory:
    def __init__(self, logger):
        self.logger = logger
        self.llm_provider = self.get_llm_provider()
        self.embedding_provider = self.get_embedding_provider()


    def get_llm_provider(self):
        if LLM_PROVIDER.lower() == "openai":
            return OpenAIProviderService(self.logger)
        elif LLM_PROVIDER.lower() == "gemini":
            return GeminiProviderService(self.logger)
        elif LLM_PROVIDER.lower() == "ollama":
            return OllamaProviderService(self.logger)
        else:
            raise ValueError(f"LLM Provider '{LLM_PROVIDER}' not supported")

    def get_embedding_provider(self):
        if EMBEDDING_PROVIDER.lower() == "openai":
            return OpenAIProviderService(self.logger)
        elif EMBEDDING_PROVIDER.lower() == "gemini":
            return GeminiProviderService(self.logger)
        elif EMBEDDING_PROVIDER.lower() == "ollama":
            return OllamaProviderService(self.logger)
        else:
            raise ValueError(f"Embedding Provider '{EMBEDDING_PROVIDER}' not supported")
