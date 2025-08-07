from src.core.repo_cloner import RepoCloner


class Orchestrator:
    def __init__(self, logger=None):
        """Orchestrates the cloning and updating of repositories."""
        self.logger = logger
        self.repo_cloner = RepoCloner(logger)

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

        except ValueError as ve:
            self.logger.error("Invalid URL or malformed parameter: %s", ve)
        except Exception:
            self.logger.exception("Unexpected error during processing")
            raise
