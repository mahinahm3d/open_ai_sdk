from dotenv import load_dotenv
load_dotenv()
from agents import Agent, Runner
from openai import AsyncOpenAI
import os

gemini_api_key = os.getenv('GEMINI_API_KEY') 

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent = Agent(
    name='Assistant',
    instructions='You are a helpul assistant.'
) 


prompt = 'Hello, how are you?'

runner = Runner.run_sync(agent,prompt)
print(runner.final_output)