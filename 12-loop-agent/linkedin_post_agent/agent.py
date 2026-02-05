"""
LinkedIn Post Generator Root Agent

This module defines the root agent for the LinkedIn post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import SequentialAgent

from .subagents.post_generator import initial_post_generator

# Create the Sequential Pipeline (will add refinement loop later)
root_agent = SequentialAgent(
    name="LinkedInPostGenerationPipeline",
    sub_agents=[
        initial_post_generator,  # Step 1: Generate initial post
    ],
    description="Generates a LinkedIn post",
)
