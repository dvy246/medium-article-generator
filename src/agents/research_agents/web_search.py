from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools
from agno.tools.youtube import YouTubeTools
from src.config.utils import model



hackernews_agent = Agent(
    name='hackernews_agent',
    tool_call_limit=3,
    instructions=[
        "You are a research assistant that gathers information from HackerNews",
        "Use the available tools to search for stories, comments, and topics as per user's request",
        "Summarize your findings clearly and concisely"
    ],
    role='hackernews_researcher',
    model=model,
    tools=[HackerNewsTools(all=True)],
    add_datetime_to_context=True
)
