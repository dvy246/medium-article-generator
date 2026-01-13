from src.workflow.workflow import wf
import asyncio

async def execute_workflow(message:str):
    try:
        output=await wf.aprint_response(input=message)

        return print(output)
    except Exception as e:
        return print(e)




asyncio.run(execute_workflow('what is the impact of artificial intelligence on the economy'))