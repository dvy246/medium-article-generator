from agno.team import Team
from src.config.utils import model
from src.agents.social_media_agents.youtube import yt_agent



yt_team=Team(
    members=[yt_agent],
    name='youtube_team',
    role='leader',
    model=model,
    instructions=['you are the leader of the youtube team and your goal is to gather information from youtube and summarize it in a clear and concise manner'],
    add_datetime_to_context=True)