from agno.agent import Agent
from src.config.utils import model
from agno.tools.wikipedia import WikipediaTools



wikipedia_agent = Agent(
    name='wikipedia_agent',
    tool_call_limit=3,
    instructions=[
        "You are a research assistant that gathers information from Wikipedia",
        "Use the available tools to search for articles, topics, and summaries as per user's request",
        "Summarize your findings clearly and concisely"
    ],
    role='wikipedia_researcher',
    model=model,
    tools=[WikipediaTools(all=True)],
    add_datetime_to_context=True
)