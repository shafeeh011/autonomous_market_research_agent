import pytest
from src.tools.web_scraper import WebScraper
from src.tools.search_tool import SearchTool
from src.tools.summarizer import Summarizer

def test_web_scraper_initialization():
    scraper = WebScraper()
    assert scraper is not None

def test_search_tool_initialization():
    search_tool = SearchTool(api_key="test_api_key")
    assert search_tool.api_key == "test_api_key"

def test_summarizer_initialization():
    summarizer = Summarizer()
    assert summarizer is not None

def test_web_scraper_scrape_function():
    scraper = WebScraper()
    data = scraper.scrape("https://example.com")
    assert isinstance(data, dict)  # Assuming scrape returns a dictionary

def test_search_tool_perform_search():
    search_tool = SearchTool(api_key="test_api_key")
    results = search_tool.perform_search("test query")
    assert isinstance(results, list)  # Assuming perform_search returns a list

def test_summarizer_summarize_function():
    summarizer = Summarizer()
    summary = summarizer.summarize("This is a test text to summarize.")
    assert isinstance(summary, str)  # Assuming summarize returns a string
    assert len(summary) > 0  # Ensure that the summary is not empty