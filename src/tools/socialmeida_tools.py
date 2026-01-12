from agno.tools.youtube import YouTubeTools
from agno.tools.reddit import RedditTools



class SocialMediaTools:
    def __init__(self, tool_name: str):

        self.tool_name=tool_name.lower().strip()

        if self.tool_name not in ['youtube','x','reddit']:
            raise ValueError("Invalid tool name")


    def initialize_tool(self, tool_name: str = None):

        target_tool = tool_name.lower().strip() if tool_name else self.tool_name

        if target_tool == 'youtube':
            return YouTubeTools(all=True)
        
        
        elif target_tool == 'reddit':
            return RedditTools()
    
    def use_multiple_tools(self, tools: list[str]):

        all_tools=[]

        for tool in tools:

            all_tools.append(self.initialize_tool(tool_name=tool))

        return all_tools