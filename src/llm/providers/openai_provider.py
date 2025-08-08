from src.llm.base_provider import BaseProviderService


class OpenAIProviderService(BaseProviderService):

    def __init__(self, logger):
        super().__init__(logger)
        self.logger = logger

    def generate_text(self, content):
        pass

    def generate_embeddings(self, content):
        pass
