from agno.tools.arxiv import ArxivTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.local_file_system import LocalFileSystemTools
from agno.tools.webtools import WebTools as AgnoWebTools
from agno.tools.newspaper4k import Newspaper4kTools
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class SearchTools:
    def __init__(self, tool_name: str):

        self.tool_name=tool_name.lower().strip()

        if self.tool_name not in ['duckduckgo','arxiv','wikipedia','hackernews','local_file_system','web']:
            raise ValueError("Invalid tool name")
        
        self.path=Path('./arxiv_papers/')

        self.path.mkdir(exist_ok=True)
        
    def initialize_tool(self, tool_name: str = None):

        target_tool = tool_name.lower().strip() if tool_name else self.tool_name

        if target_tool == 'duckduckgo':
            return DuckDuckGoTools(fixed_max_results=5,all=True)
        
        elif target_tool == 'hackernews':
            return HackerNewsTools()
        
        elif target_tool == 'arxiv':
            return ArxivTools(all=True,enable_read_arxiv_papers=True,enable_search_arxiv=True,path=self.path)
        
        elif target_tool == 'wikipedia':
            return WikipediaTools()
        
        elif target_tool == 'web':
            return AgnoWebTools()
         
        elif target_tool=='newspaper':
            return Newspaper4kTools()


    def use_multiple_tools(self, tools: list[str]):
        
        tools_to_use=[]

        for tool in tools:

            initialize=self.initialize_tool(tool_name=tool)

            tools_to_use.append(initialize)

        return tools_to_use

    
target_dir = Path("./medium_articles/")
target_dir.mkdir(exist_ok=True)

file_system=LocalFileSystemTools(target_directory=target_dir,default_extension='md')

