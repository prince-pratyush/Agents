from google.adk.agents import Agent

from .sub_agents.stock_analyst.agent import stock_analyst

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst: Can look up stock prices
    """,
    sub_agents=[stock_analyst],
)
