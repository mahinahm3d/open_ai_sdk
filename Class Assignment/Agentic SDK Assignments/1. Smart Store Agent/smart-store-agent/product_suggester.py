import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=provider)


agent = Agent(
    name="Smart Store Agent",
    instructions="You are a Smart Store Agent. Your job is to suggest products based on user needs. For example: - If the user says I have a headache, suggest a medicine like Panadol and explain why. Be helpful, concise, and explain why the product is useful.",
    model=model,
)

user_question = input("Please enter your symptoms: ")

result = Runner.run_sync(agent, user_question)

print(result.final_output)