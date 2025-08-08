from google import genai
from src.llm.base_provider import BaseProviderService
from config.conf import GEMINI_API_KEY, GEMINI_MODEL


class GeminiProviderService(BaseProviderService):

    def __init__(self, logger):
        super().__init__(logger)
        self.logger = logger

        # Validate GEMINI_API_KEY
        if not GEMINI_API_KEY:
            self.logger.error("GEMINI_API_KEY is not configured")
            raise ValueError("GEMINI_API_KEY is not configured")

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_text(self, content: str) -> str:
        try:
            # Check if GEMINI_MODEL is properly configured
            if not GEMINI_MODEL:
                self.logger.error("GEMINI_MODEL is not configured")
                return None

            response = self.client.models.generate_content(
                model=GEMINI_MODEL, 
                contents=content 
            )
            return response.text
        except Exception as e:
            self.logger.error(f"Error generating text with Gemini: {e}")
            return None

    def generate_embeddings(self, content):
        pass
