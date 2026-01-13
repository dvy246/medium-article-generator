from src.workflow.workflow import wf
import asyncio

async def execute_workflow(message: str):
    try:
        output = await wf.aprint_response(input=message)
        return output
    except Exception as e:
        print(f"Error executing workflow: {e}")
        return None

def run_workflow(topic: str):
    asyncio.run(execute_workflow(topic))
