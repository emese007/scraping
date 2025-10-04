from pipelines.pipelines_scraping import run_scraping_pipeline
from pipelines.pipelines_api import run_api_pipeline

def main():
    run_scraping_pipeline()
    run_api_pipeline()

if __name__ == "__main__":
    main()
