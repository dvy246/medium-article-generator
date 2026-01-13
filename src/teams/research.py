from src.agents.research_agents.newspaper_research import newspaper_agent
from src.agents.research_agents.arxiv_research import arxiv_agent
from src.agents.research_agents.ddg_research import duckduckgo_agent
from src.agents.research_agents.wikipedia_search import wikipedia_agent
from src.agents.research_agents.web_search import hackernews_agent
from agno.team import Team
from agno.tools.youtube import YouTubeTools
from src.config.utils import model



research_team=Team(
    members=[arxiv_agent,wikipedia_agent,hackernews_agent,newspaper_agent,duckduckgo_agent],
    name='research_team',
    role='leader',
    model=model,
    instructions=['you are the leader of the research team and your goal is to gather information from different sources and summarize it in a clear and concise manner make sure you use the filesystem tool to save the information gathered in the directory and use you sub agents like duck duck go for duck duck go search, newspaper agent to gather news articles and hackernews agent to get hacker news information and wikipedia agent to get wikipedia information and arxiv agent to get arxiv information and write the article in simple plain english wih no jargons and cite the sources also with the metrics if used  and dont give output beyond the scope of the query you get ' ],
    add_datetime_to_context=True,
    add_history_to_context=True

)