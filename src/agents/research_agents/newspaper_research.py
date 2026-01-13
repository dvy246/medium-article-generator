from agno.agent import Agent
from agno.tools.newspaper4k import Newspaper4kTools
from src.config.utils import model



newspaper_agent = Agent(
    name='newspaper_agent',
    tool_call_limit=3,
    instructions=[
        "You are a research assistant that gathers information from news articles",
        "Use the available tools to search for articles, topics, and summaries as per user's request",
        "Summarize your findings clearly and concisely"
    ],
    role='newspaper_researcher',
    model=model,
    tools=[Newspaper4kTools(include_summary=True)
],
    add_datetime_to_context=True
)