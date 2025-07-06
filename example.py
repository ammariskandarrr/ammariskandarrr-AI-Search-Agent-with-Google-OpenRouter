from search_agent import GoogleSearchAgent

agent = GoogleSearchAgent()
queries = [
    "Best LLM models 2024",
    "How to learn Python fast",
    "Latest AI news"
]

for query in queries:
    print(agent.search_and_analyze(query))
    print("\n" + "="*50 + "\n")
