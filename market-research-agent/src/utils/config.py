# Configuration settings for the market research agent

import os

class Config:
    # API keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")
    SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "your_serpapi_api_key")

    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

    # Other settings
    DEBUG = os.getenv("DEBUG", "False") == "True"
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")