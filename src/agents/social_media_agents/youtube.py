from agno.agent import Agent
from agno.team import Team
from agno.tools.youtube import YouTubeTools
from src.config.utils import model



yt_agent=Agent(
    model=model,
    name='youtube_agent',
    role='youtube_researcher',
    instructions=['you are a youtube agent that searches for videos and gives the transcript of the video'],
    tools=[YouTubeTools(all=True)
],
    add_datetime_to_context=True
)


