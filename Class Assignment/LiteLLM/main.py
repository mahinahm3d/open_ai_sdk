from dotenv import load_dotenv
import os
from litellm import completion

# Load the .env file
load_dotenv()

# Use key from environment
api_key = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_KEY"] = api_key

response = completion(
    model="openrouter/anthropic/claude-3-haiku",
    messages=[{"role": "user", "content": "What is LiteLLM?"}]
)

print(response['choices'][0]['message']['content'])
