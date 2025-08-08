from src.core.repo_cloner import RepoCloner
from src.core.repo_analyzer import RepoAnalyzer
from src.llm.factory_provider import ProviderFactory


class Orchestrator:
    def __init__(self, logger=None):
        """Orchestrates the cloning and updating of repositories."""
        self.logger = logger
        self.repo_cloner = RepoCloner(logger)
        self.repo_analyzer = RepoAnalyzer(logger)
        self.provider_factory = ProviderFactory(logger)

    def processing_repo(self, url_repo: str, token: str = None, username: str = None):
        """
        Coordinates the full pipeline:
        - Clones the repository
        - Analyzes its structure
        - Processes the code for embedding

        Args:
            url_repo (str): URL of the GitHub repository.
            token (str, optional): GitHub token if authentication is needed.
            username (str, optional): GitHub username if authentication is needed.
        """
        try:
            self.logger.info("Starting process. It may take a while...")

            cloned_repo_path, repo_name = self.repo_cloner.get_repo(
                url_repo, token, username
            )
            self.logger.info(
                "Repository name: %s, Origin: %s", repo_name, cloned_repo_path
            )

            output_json_path = self.repo_analyzer.analyze_and_export(
                cloned_repo_path, repo_name
            )
            self.logger.info("Structure exported to: %s", output_json_path)

            provider = self.provider_factory.llm_provider
            response = provider.generate_text("Tell me a joke")
            print(response)
            self.logger.info("Text generation completed successfully.")

        except ValueError as ve:
            self.logger.error("Invalid URL or malformed parameter: %s", ve)
        except Exception:
            self.logger.exception("Unexpected error during processing")
            raise
