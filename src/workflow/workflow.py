from agno.workflow import Workflow,Step,Parallel
from src.teams.research import research_team
from src.teams.social_research import yt_team
from agno.agent import Agent
from pathlib import Path
from src.config.utils import model 
from agno.tools.local_file_system import LocalFileSystemTools


medium_file=Path(__file__).parent.parent/'medium_file'

medium_file.mkdir(exist_ok=True)

agent=Agent(
    model=model,
    role='report generator',
    name='report_generator',
    instructions=['you are a report generator that generates a report based on the information gathered by the research team and the youtube team using the tools you have and save the report to the given directory in ur local file system make sure it is in simple words and engaging with no jargons and cite the sources also with the metrics if used  and dont give output beyond the scope of the query you get and make sure you dont hallucinate'],
     tools=[LocalFileSystemTools(target_directory=medium_file,default_extension='md')],
     add_datetime_to_context=True,
     id='report_generator'
)

step1=Step(
    name='step1',
    team=research_team,
    description='a team dedicated for doing research over the web'
)

step2=Step(
    name='step2',
    team=yt_team,
    description='a team dedicated for doing research over youtube'
)

paralell=Parallel(
    step1,step2,
    name='parallel',
    description='perform search on the topic given comprehensive advanced research'
)

wf=Workflow(
    id='workflow medium',
    steps=[paralell,agent],
    description='a workflow that performs comprehensive advanced research on a given topic and generates a report based on the information gathered',
    name='workflow medium'
    
)




