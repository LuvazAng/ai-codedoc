from abc import ABC, abstractmethod
from typing import List, Optional, Dict

class BaseProviderService(ABC):
    """Abstract base class for embedding service"""

    def __init__(self, logger):
        self.logger = logger 
    
    @abstractmethod
    def generate_text(self, content: str) -> str:
        pass

    @abstractmethod
    def generate_embeddings(self, content: str) -> Optional[List[float]]:
        pass