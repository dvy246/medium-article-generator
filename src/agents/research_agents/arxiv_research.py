from src.config.utils import model
from agno.agent import Agent
from src.tools.search_tools import SearchTools
from textwrap import dedent
from pathlib import Path

mistral=model.initialize_model()


tool=SearchTools(tool_name='arxiv')


arxiv_agent = Agent(
    model=mistral,
    name="arxiv_agent",
    tools=tool,
    description=