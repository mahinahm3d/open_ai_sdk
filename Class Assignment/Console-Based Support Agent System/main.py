# Load environment variables from .env file
from dotenv import load_dotenv
import os
# Context model for passing user info
from pydantic import BaseModel
# Gemini API setup
import google.generativeai as genai

# -------- Load API Key from .env --------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file!")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Load the Gemini model (can switch to gemini-1.0-pro or others if needed)
model = genai.GenerativeModel("gemini-1.5-flash") 


# -------- Context Model --------
class UserContext(BaseModel):
    name: str
    is_premium_user: bool
    issue_type: str | None = None

# -------- Tool: Refund (Billing) --------
def refund_tool(context: UserContext) -> str:
    if not context.is_premium_user:
        return "❌ Refunds are only available for premium users."
    return f"✅ Refund processed for {context.name}."

# -------- Tool: Restart Service (Technical) --------
def restart_service_tool(context: UserContext) -> str:
    if context.issue_type != "technical":
        return "❌ Service restart is only allowed for technical issues."
    return f"🔧 Service has been restarted for {context.name}."


# -------- Agent: Billing --------
def billing_agent(query: str, context: UserContext) -> str:
    if "refund" in query.lower():
        return refund_tool(context)
    return "💳 I'm the Billing Agent. I can help with billing-related issues."

# -------- Agent: Technical --------
def technical_agent(query: str, context: UserContext) -> str:
    if "restart" in query.lower() or "not working" in query.lower():
        return restart_service_tool(context)
    return "🛠️ I'm the Technical Agent. Please describe your issue in more detail."

# -------- Agent: General (AI via Gemini) --------
def general_agent(query: str, context: UserContext) -> str:
    prompt = f"You are a helpful support assistant. A user named {context.name} has asked: {query}"
    response = model.generate_content(prompt)
    return response.text.strip()

# -------- Triage Agent --------
def triage_agent(query: str) -> str:
    query = query.lower()
    if "refund" in query or "billing" in query:
        return "billing"
    elif "not working" in query or "error" in query or "restart" in query:
        return "technical"
    else:
        return "general"

# -------- CLI Main Program --------
def main():
    print("\n🎯 Welcome to the Console-Based Support Agent System\n")
    
    # Gather user info
    name = input("👤 Enter your name: ")
    is_premium_input = input("💎 Are you a premium user? (yes/no): ").lower().strip()
    is_premium = is_premium_input in ["yes", "y"]

    # Create user context
    context = UserContext(name=name, is_premium_user=is_premium)

    # Start conversation loop
    while True:
        query = input("\n💬 Ask your question (or type 'exit'): ").strip()
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Triage logic sets issue_type
        context.issue_type = triage_agent(query)
        print(f"📌 Routed to: {context.issue_type.capitalize()} Agent")

        # Agent Handoff Simulation
        if context.issue_type == "billing":
            result = billing_agent(query, context)
        elif context.issue_type == "technical":
            result = technical_agent(query, context)
        else:
            result = general_agent(query, context)

        # Output the final response
        print(f"\n🧠 Response: {result}")

# ------------------- Run App -------------------
if __name__ == "__main__":
    main()
