import pytest
from src.agents.research_agent import ResearchAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.report_agent import ReportAgent

def test_research_agent_initialization():
    agent = ResearchAgent()
    assert agent is not None

def test_research_agent_data_gathering():
    agent = ResearchAgent()
    data = agent.gather_data("business idea", "target audience")
    assert isinstance(data, dict)  # Assuming it returns a dictionary

def test_analysis_agent_initialization():
    agent = AnalysisAgent()
    assert agent is not None

def test_analysis_agent_insight_extraction():
    agent = AnalysisAgent()
    insights = agent.extract_insights({"data": "sample data"})
    assert isinstance(insights, list)  # Assuming it returns a list of insights

def test_report_agent_initialization():
    agent = ReportAgent()
    assert agent is not None

def test_report_agent_report_generation():
    agent = ReportAgent()
    report = agent.generate_report({"insights": "sample insights"})
    assert isinstance(report, str)  # Assuming it returns a string report