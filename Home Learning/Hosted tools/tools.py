# Hosted tools refers to pre-defined or sutom tools that you make available for your agent to call during reasoning or task completion.

# 1 Example: Calculator Agent.
from openai import OpenAI
from openai.agents import Agent, tool

# Define tool
@tool
def add_numbers(a: int, b: int) -> int:
    """Give sum of two numbers."""
    return a + b

# Make agent and give tool
agent = Agent(tools=[add_numbers])

# Ask question from agent
result = agent.run("What is the sum of 5 and 3?")
print(result)