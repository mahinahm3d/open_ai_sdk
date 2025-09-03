# Async Basic Agent.
from dotenv import load_dotenv
import os 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
import asyncio 


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    agent = Agent(
        name = "Assistant",
        instructions = "You are a helpfull assistant. Always Help users with their queries"
    )

    response = await Runner.run(
        agent,
        input = "What is Generative AI? tell me in one line.",
        run_config = config
    )

    print(response)
asyncio.run(main())