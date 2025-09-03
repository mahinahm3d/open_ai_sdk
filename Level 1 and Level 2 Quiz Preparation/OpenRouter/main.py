from dotenv import load_dotenv
import os 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY") 

if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

# Setup OpenRouter client (like OpenAI, but via OpenRouter)
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1", #Openrouter Base Url
)

model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528-qwen3-8b:free", #Example model, Replace if needed
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
 
agent = Agent(
    name = "Daily Motivator Agent",
    instructions = "You are a Daily Motivator Agent. That Generate motivating quotes."
)

response = Runner.run_sync(
    agent,
    input = "Motivate me”, “Quote of the day.",
    run_config = config
)

print(response)