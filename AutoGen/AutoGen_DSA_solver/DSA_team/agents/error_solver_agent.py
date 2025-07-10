from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client


model_client = get_model_client()

def get_error_solver_agent():
    """
    Function to get the error solver agent.
    This agent is responsible for solving errors in code.
    It will work with the code executor agent to execute the code.
    """
    error_solver_agent = AssistantAgent(
        name="Error_Agent",
        description="An agent that solves errors",
        model_client=model_client,
        system_message="""
            You are a error solver agent that is an expert in solving error in code and debugging.
            You will be working with code executor agent to execute code.
            Also you will be working with problem solver agent to solve DSA problems.
            You will solve general problems also and you will provide solution for those errors"""
    )
    
    return error_solver_agent