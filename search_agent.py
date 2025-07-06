import os
import json
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from llama_index.llms.openrouter import OpenRouter

class GoogleSearchAgent:
    def __init__(self):
        # Initialize with environment variables
        self.search = GoogleSearchAPIWrapper(
            google_cse_id=os.getenv("GOOGLE_CSE_ID"),
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        self.llm = OpenRouter(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            model="gryphe/mythomax-l2-13b",
            max_tokens=256
        )

    def search_and_analyze(self, query):
        """One function to handle everything"""
        print(f"\n🔍 Searching for: {query}")
        
        # 1. Perform search
        results = self.search.results(query, num_results=3)
        
        # 2. Show results
        print("\n📄 Results:")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}\n   {result['link']}")
        
        # 3. Generate summary
        summary = self.llm.complete(
            f"Summarize these in 2 sentences:\n{json.dumps(results)}"
        )
        
        return f"\n🤖 AI Summary:\n{summary.text}"

# Quick usage example
if __name__ == "__main__":
    agent = GoogleSearchAgent()
    print(agent.search_and_analyze("Python 3.12 new features"))
