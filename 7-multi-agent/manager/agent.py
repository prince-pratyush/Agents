from google.adk.agents import Agent

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.stock_analyst.agent import stock_analyst

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agents:
    - stock_analyst: Can look up stock prices
    - funny_nerd: Tells nerdy jokes about programming, math, science, etc.
    """,
    sub_agents=[stock_analyst, funny_nerd],
)
