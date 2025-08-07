from src.orchestrator import Orchestrator
from src.utils.loggers import FileLoggerConfigurator

def main():
    """Main function to set up the logger."""
    logger_configurator = FileLoggerConfigurator()
    logger = logger_configurator.setup_logger("application", level=0)
    logger.info("Logger has been set up successfully.")

    try:
        orchestrator_flow = Orchestrator(logger)
        orchestrator_flow.processing_repo("SET_SOME_URL_REPO")
    except IOError as e:
        logger.exception("An error occurred while running the application. %s", e)

if __name__ == "__main__":
    main()
