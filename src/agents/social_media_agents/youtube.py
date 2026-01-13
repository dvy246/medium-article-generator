from agno.agent import Agent
from agno.team import Team
from agno.tools.youtube import YouTubeTools
from src.config.utils import model



yt_agent=Agent(
    model=model,
    name='youtube_agent',
    role='youtube_researcher',
    instructions=['you are a youtube agent that searches for videos and gives the transcript of the video and you use the youtube tool to get the transcript of the video and its your duty to make sure the video is not too long and you give the transcript in a clear and concise manner and it matches the query and if you cant find any video then just respond i dont have any video of that topic '],
    tools=[YouTubeTools(all=True)],
    tool_call_limit=3,
    add_datetime_to_context=True
)


