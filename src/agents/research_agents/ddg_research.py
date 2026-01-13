from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from src.config.utils import model



duckduckgo_agent = Agent(
    name='duckduckgo_agent',
    tool_call_limit=3,
    instructions=[
        "You are a research assistant that gathers information using DuckDuckGo search engine",
        "Use the available tools to search for web pages, topics, and summaries as per user's request",
        "Summarize your findings clearly and concisely"
    ],
    role='duckduckgo_researcher',
    model=model,
    tools=[DuckDuckGoTools(fixed_max_results=5,cache_results=True)],
    add_datetime_to_context=True
)