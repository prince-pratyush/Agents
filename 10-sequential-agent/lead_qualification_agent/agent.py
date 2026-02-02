"""
Sequential Agent with a Minimal Callback

This example demonstrates a lead qualification pipeline with a minimal
before_agent_callback that only initializes state once at the beginning.
"""

from google.adk.agents import SequentialAgent

# Import the subagents
from .subagents.scorer import lead_scorer_agent
from .subagents.validator import lead_validator_agent

# Create the sequential agent with minimal callback
root_agent = SequentialAgent(
    name="LeadQualificationPipeline",
    sub_agents=[lead_validator_agent, lead_scorer_agent],
    description="A pipeline that validates and scores sales leads",
)
