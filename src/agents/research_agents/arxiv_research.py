from src.config.utils import model
from agno.agent import Agent
from textwrap import dedent
from agno.tools.arxiv import ArxivTools
from agno.agent import Agent
from pathlib import Path


research_path=Path(__file__).parent.parent.parent/'research'

research_path.mkdir(exist_ok=True)

arxiv_agent=Agent(name='arxiv_agent',
                  tool_call_limit=3,
                   instructions=["You are a research assistant that gathers research papers from Arxiv",
                  "Use the available tools to search for research papers, authors and topics as per user's request",
                  "Summarize your findings clearly and concisely and you can download the research paper using arxiv tool "],
                  role='arxic_researcher',
                  model=model,
                  tools=[ArxivTools(all=True,download_dir=research_path)],
                  add_datetime_to_context=True
                  )
