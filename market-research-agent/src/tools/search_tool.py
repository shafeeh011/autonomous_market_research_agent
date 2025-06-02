from serpapi import GoogleSearch

class SearchTool:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query, num_results=10):
        params = {
            "engine": "google",
            "q": query,
            "num": num_results,
            "api_key": self.api_key
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("organic_results", [])

    def extract_links(self, search_results):
        return [result["link"] for result in search_results if "link" in result]