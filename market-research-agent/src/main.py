# main.py

from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent
from tools.web_scraper import WebScraper
from tools.search_tool import SearchTool
from tools.summarizer import Summarizer
from memory.vector_store import VectorStore
from memory.persistence import Persistence
from ui.streamlit_app import run_streamlit_app
from ui.fastapi_server import run_fastapi_server

def main():
    # Initialize components
    research_agent = ResearchAgent()
    analysis_agent = AnalysisAgent()
    report_agent = ReportAgent()
    web_scraper = WebScraper()
    search_tool = SearchTool()
    summarizer = Summarizer()
    vector_store = VectorStore()
    persistence = Persistence()

    # Example workflow
    user_input = "Market research for a new coffee shop"
    audience = "Local coffee enthusiasts"

    # Step 1: Gather data
    research_data = research_agent.gather_data(user_input, audience)

    # Step 2: Analyze data
    insights = analysis_agent.extract_insights(research_data)

    # Step 3: Generate report
    report = report_agent.generate_report(insights)

    # Step 4: Display report
    run_streamlit_app(report)

if __name__ == "__main__":
    main()